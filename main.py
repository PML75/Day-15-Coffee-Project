import os
import math


espresso = 1.50
latte = 2.50
cappuccino = 2.99


coffee_machine = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0.0
}


print("You approach a coffee machine and see 3 hot beverage.")


def refill_machine(resource_name):
    if resource_name == "water":
        coffee_machine['Water'] = 300
    elif resource_name == "milk":
        coffee_machine['Milk'] = 200
    else:
        coffee_machine['Coffee'] = 100


def make_coffee(coffee_name):
    if coffee_name == "espresso":
        if coffee_machine['Water'] > 0 and coffee_machine['Coffee'] > 0:
            coffee_machine['Water'] -= 50
            coffee_machine['Coffee'] -= 18
            print("Here is your espresso \u2615. Enjoy!")
        elif coffee_machine['Water'] == 0:
            print("Sorry, there is not enough water.")
        else:
            print("sorry, there is not enough coffee beans.")
    elif coffee_name == "latte":
        if coffee_machine['Water'] > 0 and coffee_machine['Coffee'] > 0 and coffee_machine['Milk'] > 0:
            coffee_machine['Water'] -= 200
            coffee_machine['Coffee'] -= 24
            coffee_machine['Milk'] -= 150
            print("Here is your latte \u2615. Enjoy!")
        elif coffee_machine['Water'] == 0:
            print("Sorry, there is not enough water.")
        elif coffee_machine['Coffee'] == 0:
            print("Sorry, there is not enough water.")
        else:
            print("sorry, there is not enough coffee beans.")
    else:
        if coffee_machine['Water'] > 0 and coffee_machine['Coffee'] > 0:
            coffee_machine['Water'] -= 250
            coffee_machine['Coffee'] -= 24
            coffee_machine['Milk'] -= 100
            print("Here is your cappuccino \u2615. Enjoy!")
        elif coffee_machine['Water'] == 0:
            print("Sorry, there is not enough water.")
        elif coffee_machine['Coffee'] == 0:
            print("Sorry, there is not enough water.")
        else:
            print("sorry, there is not enough coffee beans.")


def check_money(money_inserted, coffee_name):
    if coffee_name == "espresso":
        if money_inserted == espresso:
            make_coffee(coffee_name)
            coffee_machine['Money'] += round(money_inserted, 2)
        elif money_inserted > espresso:
            money_change = round((money_inserted - espresso), 2)
            coffee_machine['Money'] += money_inserted - money_change
            print(f"Here is change of ${money_change}.")
            make_coffee(coffee_name)
        else:
            print("Sorry, that's not enough money. Money refunded.")
    if coffee_name == "latte":
        if money_inserted == latte:
            make_coffee(coffee_name)
            coffee_machine['Money'] += round(money_inserted, 2)
        elif money_inserted > latte:
            money_change = money_inserted - latte
            coffee_machine['Money'] += round((money_inserted - money_change), 2)
            print(f"Here is change of ${money_change}.")
            make_coffee(coffee_name)
        else:
            print("Sorry, that's not enough money. Money refunded.")
    if coffee_name == "cappuccino":
        if money_inserted == cappuccino:
            make_coffee(coffee_name)
            coffee_machine['Money'] += round(money_inserted, 2)
        elif money_inserted > cappuccino:
            money_change = money_inserted - cappuccino
            coffee_machine['Money'] += round((money_inserted - money_change), 2)
            print(f"Here is change of ${money_change}.")
            make_coffee(coffee_name)
        else:
            print("Sorry, that's not enough money. Money refunded.")


def turn_off():
    return False


def report():
    for key in coffee_machine:
        if key == "Water" or key == "Milk":
            print(f"{key}: {coffee_machine[key]}ml")
        elif key == "Coffee":
            print(f"{key}: {coffee_machine[key]}g")
        else:
            print(f"{key}: ${coffee_machine[key]}")


def start_coffee():
    global coffee_machine
    coffee_machine = {
        "Water": 300,
        "Milk": 200,
        "Coffee": 100,
        "Money": 0.0
    }
    coffee_functional = True
    print("Espresso ($1.50) / Latte ($2.50) / Cappuccino ($2.99)")
    while coffee_functional:
        prompt_coffee = input("\nWhat would you like? (espresso/latte/cappuccino): ")
        get_resource = prompt_coffee.split(" ")
        get_refill = get_resource[0]
        if prompt_coffee == "report":
            report()
        elif prompt_coffee == "off":
            coffee_functional = turn_off()
        elif get_refill == "refill":
            resource_name = get_resource[1]
            refill_machine(resource_name)
        else:
            print("Please insert coin.")
            quarters_insert = int(input("How many quarters?: "))
            dimes_insert = int(input("How many dimes?: "))
            pennies_insert = int(input("How many pennies?: "))

            total_money = ((quarters_insert*0.25)+(dimes_insert*0.10)+(pennies_insert*0.01))
            check_money(total_money, prompt_coffee)
            # if check_money:
            #     coffee_machine['Money'] += round(total_money, 2)
            #     make_coffee(prompt_coffee)


start_coffee()
