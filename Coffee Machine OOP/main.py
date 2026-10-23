from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffemaker = CoffeeMaker()
money = MoneyMachine()
menu_items = menu.get_items()
is_on = True

while is_on:
    choice = input(f"What would you like? ({menu_items}): ")
    drink = menu.find_drink(choice)
    if choice == "off":
        is_on = False
        print("Machine is turned OFF.")
    elif choice == "report":
        coffemaker.report()
        money.report()
    elif drink:
        cost = drink.cost
        if coffemaker.is_resource_sufficient(drink) and money.make_payment(cost):
            coffemaker.make_coffee(drink)
    else:
        print("Enter a valid input.")