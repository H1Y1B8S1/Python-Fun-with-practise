import time
import random


class Warship:
    def __init__(self, index, country, crew=None, is_sunk=False, hits=0, kits=1):
        self.index = index
        self.country = country
        self.crew = crew
        self.is_sunk = is_sunk
        self.hits = hits
        self.kits = kits
        self.name = self.country + str(self.index)

    def get_shot(self):
        self.hits += 1
        return self

    def sink(self):
        dk_swimming = []
        k_swimming = []
        print("\n" + self.name + ' is sinking...')
        floating = self.crew_out()
        return floating

    def crew_out(self):
        floating_men = []
        for man in self.crew:
            man.in_water = True
            floating_men.append(man)
        return floating_men

    def fire(self, target):
        print("Ship {} fired {}".format(self.name, target.name))
        target.hits += 1


class Man:
    def __init__(self, index, ship, swims=None, in_water=None, has_kit=None):
        self.index = index
        self.ship = ship
        self.swims = swims
        self.in_water = in_water
        self.has_kit = has_kit
        self.name = str(index) + '_' + self.ship.name

    def die(self):
        self.ship.crew.remove(self)
        del self

    def take_refuge(self, ship):
        old_name = self.name
        old_ship = self.ship
        new_ship = ship
        new_ship.crew.append(self)
        self.ship = new_ship
        self.name = str(len(new_ship.crew)) + '_' + self.ship.name
        print("Man {} moved from {} to {}".format(old_name, old_ship.name, new_ship.name))

    def surrender(self, ship):
        old_name = self.name
        old_ship = self.ship
        new_ship = ship
        new_ship.crew.append(self)
        new_ship.kits += 1
        self.ship = new_ship
        self.name = str(len(new_ship.crew)) + '_' + self.ship.name
        print("Man {} surrendered to {}".format(old_name, new_ship.name))


class Shark:
    def __init__(self, name):
        self.name = name

    def hunt(self, target):
        print("Shark has killed {}".format(target.name))
        target.die()


def select_random(group):
    return random.choice(group)


def initiate_warships():
    a1 = Warship(1, 'a')
    a2 = Warship(2, 'a')
    a3 = Warship(3, 'a')
    b1 = Warship(1, 'b')
    b2 = Warship(2, 'b')
    b3 = Warship(3, 'b')
    b4 = Warship(4, 'b')
    b5 = Warship(5, 'b')
    c1 = Warship(1, 'c')
    c2 = Warship(2, 'c')
    c3 = Warship(3, 'c')
    d1 = Warship(1, 'd')
    d2 = Warship(2, 'd')
    d3 = Warship(3, 'd')
    d4 = Warship(4, 'd')
    e1 = Warship(1, 'e')
    e2 = Warship(2, 'e')
    e3 = Warship(3, 'e')
    f1 = Warship(1, 'f')
    f2 = Warship(2, 'f')
    g1 = Warship(1, 'g')
    g2 = Warship(2, 'g')
    x1 = Warship(1, 'x')
    y1 = Warship(1, 'y')
    z1 = Warship(1, 'z')
    a_land = [a1, a2, a3]
    b_land = [b1, b2, b3, b4, b5]
    c_land = [c1, c2, c3]
    d_land = [d1, d2, d3, d4]
    e_land = [e1, e2, e3]
    f_land = [f1, f2]
    g_land = [g1, g2]
    x_land = [x1]
    y_land = [y1]
    z_land = [z1]
    countries = [a_land, b_land, c_land, d_land,
                 e_land, f_land, g_land, x_land, y_land, z_land]
    return countries


def print_gameboard(countries):
    for country in countries:
        for ship in country:
            print('Ship ' + ship.name + ': ' + str(len(ship.crew)) + ' men')
    print("###############################################################")


def initiate_instances(ships):
    for ship in ships:
        for i in range(3):
            if ship.crew is None:
                ship.crew = []
            man = Man(index=i, ship=ship, swims=random.choice([True, False]))
            ship.crew.append(man)


def allies(man, ships):
    allies = []
    for ship in ships:
        if man.ship.country == ship.country:
            if man.ship != ship:
                allies.append(ship)
    return allies


def enemies(man, ships):
    enemies = []
    for ship in ships:
        if man.ship.country != ship.country:
            enemies.append(ship)
    return enemies


def get_country_by_name(name, countries):
    for country in countries:
        if country[0].country == name:
            return country


def country_lose(country, countries):
    countries.remove(country)
    del country
    return countries


def handle_floating_men(floating_men, ships, shark):
    man = random.choice(floating_men)
    for kit in range(man.ship.kits):
        man.has_kit = True
        print("Man {} got the kit".format(man.name))
        man.ship.kits -= 1
    shark_bites = random.choice([0, 1])
    if shark_bites == 1:
        shark_target = select_random(floating_men)
        shark.hunt(shark_target)
        floating_men.remove(shark_target)

    ally_ships = allies(man, ships)
    enemy_ships = enemies(man, ships)

    for man in floating_men:
        if len(ally_ships) != 0:  # allies exist
            if man.swims or man.has_kit:
                refuge_target_ship = select_random(ally_ships)
                man.take_refuge(refuge_target_ship)
            else:
                print(man.name + ' drowned')
                man.die()
        else:
            if man.swims or man.has_kit:
                surrender_target_ship = select_random(enemy_ships)
                man.surrender(surrender_target_ship)
            else:
                print(man.name + ' drowned')
                man.die()


def firing_round(ships, shark):
    print("---------------------------")
    # time.sleep(1)
    shooter_ship = select_random(ships)
    target_ship = select_random(ships)
    while shooter_ship.country == target_ship.country:
        target_ship = select_random(ships)
    shooter_ship.fire(target_ship)
    print("Ship {} has been shot {} time(s)".format(
        target_ship.name, target_ship.hits))
    if target_ship.hits == 2:
        handle_floating_men(target_ship.sink(), ships, shark)
        print("{} :: We Are STRONG".format(shooter_ship.name))
        print("Ship {} sunk...".format(target_ship.name))
        return target_ship


def main():
    shark = Shark('rex')
    playing_countries = initiate_warships()
    playing_ships = [ship for country in playing_countries for ship in country]
    initiate_instances(playing_ships)
    print_gameboard(playing_countries)
    while len(playing_countries) > 1:
        country_remaining_ships = []
        ship_died = firing_round(playing_ships, shark)
        if ship_died:  # if any ship got sunk
            country_died = get_country_by_name(
                ship_died.country, playing_countries)
            country_died_id = playing_countries.index(country_died)
            playing_ships.remove(ship_died)
            playing_countries[country_died_id].remove(ship_died)
            for ship in playing_ships:
                if ship.country == ship_died.country:  # if ally ship exists
                    country_remaining_ships.append(ship)
            if len(country_remaining_ships) == 0:  # country lost the war
                print("{} LOST THE WAR".format(ship_died.country))
                playing_countries = country_lose(country_died, playing_countries)
            else:
                print("###---Country {} has {} ships left---###".format(
                    ship_died.country, len(playing_countries[country_died_id])))
            del ship_died
    return playing_countries


start = time.perf_counter()
winner = main()
finish = time.perf_counter()

print('####################################\n\n')
print("COUNTRY {} HAS WON THE WAR WITH {} SHIP(S)".format(winner[0][0].country, len(winner)))
print('\n\n####################################')
print("Script finished in " + str(round(finish - start, 2)) + " seconds")
