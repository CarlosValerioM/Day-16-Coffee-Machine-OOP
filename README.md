# Day-16-Coffee-Machine
Your Coffee Machine - Difficulty: Intermediate
# CoffeeMachine

## Author:
Carlos Valerio (CarlosValerioM)

## Date:
2025/03/18

## License:
MIT License

## Dependencies:
None (built-in functions only)

## Description:
`coffee_machine.py` is a Python script that simulates a coffee machine. It allows the user to choose between different coffee options, such as espresso, latte, and cappuccino, by interacting with the CoffeeMachine class. It manages the available ingredients, checks if there's enough stock, and prepares the selected coffee. The script includes functionality to print a report of the remaining ingredients and ensures that the correct amount of ingredients is used.

The CoffeeMachine class is responsible for making coffee and tracking the remaining resources, while the Coffee class represents the coffee options (such as espresso, latte, and cappuccino), including the required ingredients.

## Usage:

1. Clone this repository:

```bash
git clone https://github.com/CarlosValerioM/Day-2-Coffee-Machine.git
```
Navigate to the project directory:
```bash
cd Day-2-Coffee-Machine
```
Run the script:

```bash
python coffee_machine.py
```
The script will prompt you for input, and based on your responses, it will prepare the requested coffee, or print a report of the current resources.

Example Output:
```bash
What would you like to order: (espresso, latte, cappuccino): latte
Enjoy your latte

What would you like to order: (espresso, latte, cappuccino): report
water: 950ml
milk: 50ml
coffee: 76g
```
How it works:
1. The script first initializes a CoffeeMachine instance with the available ingredients (water, milk, and coffee).
2. The user is prompted to input their desired coffee type (espresso, latte, cappuccino).
3. The make_coffee method checks if there are enough ingredients for the selected coffee.
4. If enough ingredients are available, it prepares the coffee and updates the stock.
5. The user can also input "report" to view the current stock of ingredients.

## License:
This project is licensed under the MIT License.
