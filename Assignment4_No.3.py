# Assignment 4
# Create a new repository in github 
# Redo the programs on assignment 2 but now with functions that return multiple values (move all user inputs in one function)

def getInput():
    total_moneyF = int(input("How much money do you have?:"))
    apple_priceF = int(input("How much does an apple cost?:"))
    maximum_applesF = int(total_moneyF/apple_priceF)
    remaining_moneyF = total_moneyF-maximum_applesF*apple_priceF
    return total_moneyF, apple_priceF, maximum_applesF, remaining_moneyF

def display(maximum_applesZ, remaining_moneyZ):
    print(f"You can buy {maximum_applesZ} apples and your change is {remaining_moneyZ} pesos")

total_money, apple_price, maximum_apples, remaining_money = getInput()
display(maximum_apples, remaining_money)
