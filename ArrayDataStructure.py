""" EXERCISE: Array DataStructure"""
"""
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this.
"""

# Let us say your expense for every month are listed below.

expense = {'january': 2200, 'february': 2350, 'march': 2600, 'april': 2130,
           'may': 2190}


def comparison(F_month, S_month):
    """ In month, how many dollars you spent extra compare to another month."""
    value = int(F_month - S_month)
    if value > 0:
        print(f'You spent {value} more dollar.')
    else:
        print(f'You spent {value} less dollar.')


def TotalExpense():
    """Will return total amount of calculated months."""
    total = sum(expense.values())
    months = len(expense.keys())
    print(f'Total expense of {months} months is : {total}\n')


# firstMonth = str(input("Enter your first month: "))
# secondMonth = str(input("Enter your second month: "))
# try:
#     comparison(expense[firstMonth], expense[secondMonth])
# except KeyError:
#     print("Please Enter valid value!!\n")
#
#
# x = input("Do you want to know total expense, If you..Press 'y': ")
# if x == 'y':
#     TotalExpense()
# else:
#     print("No problem, as your wish.")

expense['june'] = 1980
expense['april'] = 1930
print(expense)
