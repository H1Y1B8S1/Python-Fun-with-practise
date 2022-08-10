
class BankAccount(object):

    def __init__(self,balance,InRate):
        self.balance = balance
        self.InRate = InRate
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Amount deposit:{amount}. Now total fund: {(self.balance):.2f}")

    def withdraw(self,amount):
        if self.balance <amount:
            print("Insufficient funs:\nCharging a $5 fee")
            if self.balance<5:
                self.balance = 0
            else:
                self.balance -= 5
        else:
            self.balance -= amount
            print(f"Total fund left: {(self.balance):.2f}")

    def display_account_info(self):
        print(f'Balance: ${(self.balance):.2f}')

    def yield_interest(self):
        if self.balance > 0:
            self.balance *=(1+self.InRate)

interestRate1 = 0.07

Acount1 = BankAccount(0, interestRate1)

syn = True
while syn:
    print("HELLO!, Welcome to our XYZ bank!!!\nPlease enter your Acount Name:")
    name = input(">>")
    print("Please choose:\nDeposit\t  or \tWithdraw")
    work = input(">>")
    if work == "Deposit" or work =='Withdraw':
        syn = False
    else:
        print("Invalid input>>\n")

if work == 'Deposit':
    deposit = int(input("Enter amount you want to deposit: "))
    Acount1.deposit(deposit)
    Acount1.yield_interest()
    Acount1.display_account_info()
elif work == 'Withdraw':
    withdraw = int(input("Enter amount you want to withdraw: "))
    Acount1.withdraw(withdraw)
    Acount1.yield_interest()
    Acount1.display_account_info()
else:
    print("Invalid input<<")
