MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
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
    }
}

resources = {
    "water": 400,
    "milk": 200,
    "coffee": 100,
}

is_on = True
is_insufficient = False
profit = 0


def show_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Insufficient resources for this choice!")
            print(f"  {order_ingredients[item]}  {resources[item]}")
            return False
    return True


def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")


def process_coins():
    quarters = int(input("Enter quarters: "))
    dimes = int(input("Enter dimes: "))
    nickles = int(input("Enter nickles: "))
    pennies = int(input("Enter pennies: "))
    total_paid = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total_paid < drink['cost']:
        print("Sorry thats not enough money!")
    else:
        change = round(total_paid - drink['cost'], 2)
        print(f"Here is your change amount: $ {change}")
        global profit
        profit += drink['cost']


while is_on:
    choice = input("what would you like? Espresso/Latte/Cappuccino ").lower()
    if choice != 'off' and choice != 'report' and choice != 'espresso' and choice != 'latte' and choice != 'cappuccino':
        print("Enter the valid input value!")
    else:
        if choice == 'off':
            print("The Machine is not working. In Maintainence!")
            is_on = False
        elif choice == 'report':
            show_resources()
        else:
            drink = MENU[choice]
            if check_resources(drink["ingredients"]):
                process_coins()
                make_coffee(drink["ingredients"])





