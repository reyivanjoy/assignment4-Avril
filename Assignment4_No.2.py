# Assignment 4
# Create a new repository in github 
# Redo the programs on assignment 2 but now with functions that return multiple values (move all user inputs in one function)

def getInfo():
    apple_priceF = int(20)
    orange_priceF = int(25)
    applesF = int(input("How many apples would you like to buy?:"))
    orangesF = int(input("How many oranges would you like to buy?:"))
    total_amountF = apple_priceF*applesF+orange_priceF*orangesF
    return apple_priceF, orange_priceF, applesF, orangesF, total_amountF

def display(total_amountZ):
    print(f"The total amount is {total_amountZ} pesos")

apple_price, orange_price, apples, oranges, total_amount = getInfo()
display(total_amount)

