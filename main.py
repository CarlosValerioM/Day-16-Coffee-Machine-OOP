#!/usr/bin/env python3
"""
coffee_machine.py - A simple coffee machine simulator.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/18
License: MIT
Dependencies: None (built-in functions only)

Description:
This script simulates a coffee machine. It allows the user to order coffee from a menu (espresso, latte, cappuccino)
and processes the order based on available resources. The program keeps track of resources like water, milk, and coffee
and updates them after each order. It also has a report function to display current resource levels.

Usage:
Run the script and follow the prompts:
    python coffee_machine.py

Example Output:
    What would you like to order: (espresso, latte, cappuccino): latte
    Enjoy your latte
"""

from coffee import Coffee
from coffee_machine import CoffeeMachine
from menu import MENU


def main():
    """
    Main function that simulates ordering and making coffee.
    It initializes the coffee machine and provides options to the user.
    """
    menu = MENU  # Load the menu containing different coffee types and ingredients
    # Initialize a CoffeeMachine object with the available ingredients
    machine = CoffeeMachine({
        "water": [1000, "ml"],
        "milk": [200, "ml"],
        "coffee": [100, "g"],
    })

    machine_on = True  # Flag to keep the machine running
    while machine_on:
        # Prompt the user for their coffee order
        order = input("What would you like to order: (espresso, latte, cappuccino): ")

        if order == "report":
            # Display the current status of the ingredients in the machine
            machine.get_report()
        else:
            # Create a Coffee object based on the selected menu option
            coffee_order = Coffee.from_menu(order, menu)

            if coffee_order:  # If the coffee was found in the menu
                # Attempt to make the coffee
                made = machine.make_coffee(coffee_order)
                if made == 1:
                    print(f"Enjoy your {order}")
            else:
                print("Sorry, that option is not available.")  # Handle invalid coffee order


if __name__ == '__main__':
    main()