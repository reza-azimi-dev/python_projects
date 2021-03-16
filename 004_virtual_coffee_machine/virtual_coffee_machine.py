import time
import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    },
}

resources = {
    "water": 250,
    "milk": 300,
    "coffee": 100,
    "money": {
        "1c": 0,
        "5c": 0,
        "10c": 0,
        "20c": 0,
        "50c": 0,
        "1e": 0,
        "2e": 0,
    }
}


# TODO: 1. print coffee machine resources
def print_resources(resource):
    print("Water:\t", str(resource["water"]) + "ml")
    print("Milk:\t", str(resource["milk"]) + "ml")
    print("Coffee:\t", str(resource["coffee"]) + "g")
    print("Money:\t", str(total_coins(resource)) + " €")


# TODO: 1.2 add resources to the machine
def add_resources(resource, checked_res):
    for i in checked_res:
        amount = int(input(f"Enter the amount of {i} you want to fill:\n"))
        resource[i] += amount


# TODO: 2. check resources sufficient?
def check_resources(resource, menu, order):
    list_of_requirements = []
    if resource["water"] < menu[order]["ingredients"]["water"]:
        list_of_requirements.append("water")
    if resource["milk"] < menu[order]["ingredients"]["milk"]:
        list_of_requirements.append("milk")
    if resource["coffee"] < menu[order]["ingredients"]["coffee"]:
        list_of_requirements.append("coffee")

    return list_of_requirements


# TODO: 3. process coins.
def total_coins(resource):
    total_money = (resource["money"]["1c"] * 1) + \
                  (resource["money"]["5c"] * 5) + \
                  (resource["money"]["10c"] * 10) + \
                  (resource["money"]["20c"] * 20) + \
                  (resource["money"]["50c"] * 50) + \
                  (resource["money"]["1e"] * 100) + \
                  (resource["money"]["2e"] * 200)
    return float(total_money / 100)


def load_coins(resource):
    while True:
        try:
            coin = str(input('Please insert coins: (1c,5c,10c,20c,50c,1e,2e)\nor press \'x\' when you\'re done!\n'))
            if coin == 'x':
                break
            resource["money"][coin] += 1
        except KeyError:
            print("Use a valid coin please (1c,5c,10c,20c,50c,1e,2e)")
            time.sleep(1.5)
        print("Your balance: ", total_coins(resources), "€")


def reset_coins(resource):
    resource["money"]["1c"] = 0
    resource["money"]["5c"] = 0
    resource["money"]["10c"] = 0
    resource["money"]["20c"] = 0
    resource["money"]["50c"] = 0
    resource["money"]["1e"] = 0
    resource["money"]["2e"] = 0


# TODO: 4. check transaction successful?
# checks if your total coins exceeds the cost of the coffee.
def check_balance(resource, menu, order):
    return total_coins(resource) > menu[order]["cost"]


# TODO: 5. make coffee
while True:
    os.system('cls')
    reset_coins(resources)
    print("Your balance: ", str(total_coins(resources)) + "€")
    while True:

        load_coins(resources)
        while True:
            list_of_coffees = ["espresso", "latte", "cappuccino", "report"]
            select_menu = input(
                "\nChoose your Coffee:\nespresso: 1.5€\nlatte: 2.5€\ncappuccino: 3.0€ \n" +
                "or type 'report' for more INFO about resources:\n")

            if select_menu not in list_of_coffees:
                print("Please select only from the given list:")
                time.sleep(3)
                continue
            break

        if select_menu == "report":
            print_resources(resources)
            continue
        else:
            if check_balance(resources, MENU, select_menu):
                # returning list of resources that need to be filled.
                checked_resources = check_resources(resources, MENU, select_menu)
                if len(checked_resources) != 0:
                    print("Please check the following: ", checked_resources)
                    add_resources(resources, checked_resources)
                    continue

                elif len(checked_resources) == 0:
                    # calculating the use of resources
                    change = total_coins(resources) - MENU[select_menu]["cost"]
                    resources["water"] -= MENU[select_menu]["ingredients"]["water"]
                    resources["milk"] -= MENU[select_menu]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[select_menu]["ingredients"]["coffee"]
                    print_resources(resources)
                    print("Your Coffee is getting ready...")
                    time.sleep(1.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    print(f"Here is your {change}€ change.")
                    time.sleep(1)
                    print(f"Here is your {select_menu.title()}! Enjoy!")
                    time.sleep(2)
                    print("Wait a moment please")
                    time.sleep(3)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    break

            else:
                print("Not enough Balance")
