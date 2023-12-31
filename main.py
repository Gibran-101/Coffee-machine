# COFFEE VENDING MACHINE
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "profit": 0
}

coffee_machine_on = True
while coffee_machine_on:

    def resource_mgr(coffee_type):
        """This function updates the resources according the user_choice"""
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]


    def options(types_of_coffees):
        """It takes user choice as input and calculates the money given by user to buy a drink and prepare the coffee"""
        if types_of_coffees == "report":
            print(f'Water: {resources["water"]} ml\n '
                  f'Milk: {resources["milk"]} ml\n '
                  f'Coffee: {resources["coffee"]} g\n '
                  f'Profit: ${resources["profit"]}')
        else:
            for drink in MENU[types_of_coffees]["ingredients"]:
                if resources[drink] < MENU[types_of_coffees]["ingredients"][drink]:
                    print(f"Sorry there is no enough {drink} ")
                    exit()
            else:
                price_of_coffee = MENU[types_of_coffees]["cost"]
                print("Please enter coins: ")
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickels = int(input("How many nickels? "))
                pennies = int(input("How many pennies? "))
                total_cash = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
                if total_cash >= price_of_coffee:
                    remaining_change = round(total_cash - price_of_coffee, 2)
                    print(f"Here is ${remaining_change} in change.")
                    print(f"Here is your {types_of_coffees}. Enjoy!”.")
                    resources["profit"] += price_of_coffee
                    resource_mgr(types_of_coffees)
                else:
                    print("Sorry that's not enough money. Money Refunded!")
                    coffee_machine_on = False


    user_choice = input("What would you like? (espresso/latte/cappuccino) or would you like to check the report: ").lower()
    options(user_choice)
