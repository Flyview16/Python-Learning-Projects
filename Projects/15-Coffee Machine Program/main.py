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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def is_resource_sufficient(order_ingredients):
    """Checks if resources are enough to make next order"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True


def process_coins():
    """Calculates coins inserted and returns total value"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_payment_successful(money_received, drink_cost):
    """Returns true if payment is successful, else false"""
    if money_received >= drink_cost:
        if money_received > drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def print_report(resources):
    for item in resources:
       print(f"{item}: {resources[item]}")


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}☕")

machine_on = True

while machine_on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "report":
        print_report(resources)
    elif prompt == "off":
        machine_on = False
    else:
        drink = MENU[prompt]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_payment_successful(payment, drink["cost"]):
                make_coffee(prompt, drink["ingredients"])

    
