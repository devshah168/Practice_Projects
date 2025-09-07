menu = {
    "espresso": {
        "ingredients": {
            "water": 5,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee":24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}
coffee_machine={
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0,
}

coins={
    "penny":0.01,
    "nickel":0.05,
    "dime":0.10,
    "quarter":0.25,
}
def check_coffee(choice):
    ingredientsneed=menu[choice]["ingredients"]
    for item in ingredientsneed:
        if ingredientsneed[item] > coffee_machine[item]:
            print(f"Sorry there is not enough {item} to make a {choice}")
            return False

def make_coffee(choice):
    ingredientsneed = menu[choice]["ingredients"]
    for item in ingredientsneed:
            coffee_machine[item] -= ingredientsneed[item]
    print(f"Here is your {choice}.Enjoy!")
    return True
def check_cost(penny,nickel,dime,quarter,choice):
    total = penny * 0.01 + nickel * 0.05 + dime *0.1+quarter*0.25
    if total < menu[choice]["cost"]:
        print(f"Sorry that is not enough money, money refunded")
        return False

def cost(penny,nickel,dime,quarter,choice):
    total = penny * 0.01 + nickel * 0.05 + dime * 0.1 + quarter * 0.25
    change = total - menu[choice]["cost"]
    coffee_machine["money"]+=menu[choice]["cost"]
    if change>0:
        print(f"Here is your ${change} in change")

i=0
while i<1:
    choice=input("What would you like?(espresso/latte/cappuchino): ")
    if choice in menu:
        if check_coffee(choice)==False:
            i=1
        else:
            print("Please enter coins")
            penny=int(input("How many pennies?: "))
            nickel=int(input("How many nickels?: "))
            dime=int(input("How many dimes?: "))
            quarter=int(input("How many quarters?: "))
            if check_cost(penny,nickel,dime,quarter,choice)==False:
                i=1
            else:
                cost(penny,nickel,dime,quarter,choice)
            make_coffee(choice)
            i=0
    elif choice=="report":
        print(coffee_machine)
        i=0
    elif choice=="switch off":
        i=1
    else:
        print("Invalid choice")
