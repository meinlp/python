import subprocess as s
import data

s.call("clear")
profit = 0
online = True


def report():
    """Just reports resources on the screen"""
    print(f"Water:  {data.resources['water']}")
    print(f"Milk:   {data.resources['milk']}")
    print(f"Coffee: {data.resources['coffee']}")
    print(f"Money:  ${profit}")


def resource_check(choice):
    """checks if resources are enough for user's choice, returns ok or name of missing ingredient"""
    ingredients = data.MENU[choice]['ingredients']
    for i in ingredients:
        if data.resources[i] < ingredients[i]:
            return i
    return "ok"


def process_coins():
    """asks user for coins and calculates the total amount of money"""
    total = 0
    print("Please,insert coins")
    for coin in data.coins_value:
        total += (int(input(f"how many {coin}s?: ")) * data.coins_value[coin])
    return total


def make_coffee(choice):
    """changes values of remain resources"""
    ingredients = data.MENU[choice]['ingredients']
    for i in ingredients:
        data.resources[i] -= ingredients[i]


while online:
    users_choice = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if users_choice == "off":
        print("Bye!")
        online = False
    elif users_choice == "report":
        report()
    else:
        if resource_check(users_choice) == "ok":
            money_received = process_coins()
            drink_cost = data.MENU[users_choice]["cost"]
            if money_received >= drink_cost:
                make_coffee(users_choice)
                profit += drink_cost
                if money_received > drink_cost:
                    change = "{:.2f}".format(money_received - drink_cost)
                    print(f"Here is ${change} in change")
                print(f"Here is your {users_choice}. Enjoy! ☕️")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry, there is not enough {resource_check(users_choice)}")
