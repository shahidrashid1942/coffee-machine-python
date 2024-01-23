from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffemaker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffemaker.report()
        money_machine.report()
    elif choice == "espresso" or "latte" or "cappuccino":
        drink = menu.find_drink(choice)
        if coffemaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffemaker.make_coffee(drink)