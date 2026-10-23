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
    "money" : 0
}

def coffee(drink):
    available = True
    ingredients = MENU[drink]["ingredients"]
    cost = MENU[drink]["cost"]
    for res, amount in ingredients.items():
        if resources[res] < amount:
            print(f"Sorry there is not enough {res}")
            available = False
            break
    if available:
        print("Insert Coins:")
        quarters = int(input("Quarters: "))
        dimes = int(input("Dimes: "))
        nickles = int(input("Nickels: "))
        pennies = int(input("Pennies: "))
        money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
        if money < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            if money > cost:
                refund = round(money - cost, 2)
                print(f"Here is ${refund} dollars in change.")
            resources["money"] += cost
            for item in ingredients:
                resources[item] -= ingredients[item]
            print(f"Here is your {drink} ☕. Enjoy!")
    



machine = True
while machine:
    want = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if want == "off":
        machine = False
        print("Machine is turned OFF.")
    elif want == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${resources['money']}")
    elif want in MENU:
        coffee(want)
    else:
        print("Enter a valid input.")