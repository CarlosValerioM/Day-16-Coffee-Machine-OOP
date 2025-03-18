class CoffeeMachine:
    """
    Represents a coffee machine with ingredients and functionality to make coffee.
    """

    def __init__(self, ingredients):
        """
        Initializes the CoffeeMachine object with the available ingredients.

        :param ingredients: A dictionary of ingredients and their available quantities
        """
        self.ingredients = ingredients

    def __str__(self):
        """
        Returns a string representation of the available ingredients in the coffee machine.
        """
        return f"{self.ingredients}"

    def get_report(self):
        """
        Prints a report of the current ingredients and their quantities in the coffee machine.
        """
        for ingredient, (quantity, unit) in self.ingredients.items():
            print(f"{ingredient}: {quantity}{unit}")

    def set_quantity(self, ingredient, used_quantity):
        """
        Decreases the quantity of a specific ingredient in the machine by the used amount.

        :param ingredient: The name of the ingredient to update
        :param used_quantity: The quantity of the ingredient used in making the coffee
        """
        self.ingredients[ingredient][0] -= used_quantity

    def make_coffee(self, order):
        """
        Tries to make the coffee based on the order's ingredients.

        :param order: The Coffee object representing the coffee to be made
        :return: 1 if the coffee was successfully made, 0 if there were not enough ingredients
        """
        # Check if there are enough ingredients for the coffee order
        for ingredient, quantity in order.ingredients.items():
            if quantity > self.ingredients[ingredient][0]:
                print(f"Sorry! There is not enough {ingredient}")
                return 0  # Return 0 if any ingredient is insufficient

        # If there are enough ingredients, proceed to make the coffee
        for ingredient, quantity in order.ingredients.items():
            self.set_quantity(ingredient, quantity)

        return 1  # Return 1 if the coffee was successfully made
