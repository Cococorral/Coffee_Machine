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
}


# TODO: 1. Print input for coffee and money type

money_count = 0

cafecito = True

while cafecito:

    coffee = input("What would you like? (espresso, latte or capuccino): ").lower()
    if coffee == "report":
        for key, value in resources.items():
            print(f"{key} : {value}")
        print(f"Money : ${money_count}")
        break
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))



    # TODO: 2. Associate the ingredients used for the selected coffee to the current supply and if there's enough, subtract.


    resources["water"] = resources["water"] - MENU[coffee]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]
    if coffee != "espresso":
        resources["milk"] = resources["milk"] - MENU[coffee]["ingredients"]["milk"]


    if resources["water"] < 0 or resources["coffee"] < 0 or resources["milk"] < 0:
        if resources["water"] < 0:
            print("Add water")
        elif resources["coffee"] < 0:
            print("Add coffee")
        elif resources["milk"] < 0:
            print("Add milk")
        break


    # TODO: 3. Associate the amount of money provided with the cost of the selected coffee and check if it's enough

    money_inserted = (quarters * 25 + dimes * 10 + nickels * 5 + pennies) / 100
    change = round(money_inserted - MENU[coffee]["cost"], 2)

    if MENU[coffee]["cost"] > money_inserted:
        print("Sorry not enough coins. Money refunded\n")
    elif MENU[coffee]["cost"] <= money_inserted:
        money_count += MENU[coffee]["cost"]
        print("\n")
        print(f"Here's ${change} change.")
        print(f"Enjoy your {coffee}!\n")

