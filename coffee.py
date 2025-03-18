class Coffee:
    """
    Represents a coffee order with its name and required ingredients.
    """

    def __init__(self, name, ingredients):
        """
        Initializes the Coffee object with its name and ingredients.

        :param name: The name of the coffee (e.g., espresso, latte)
        :param ingredients: The ingredients and their quantities required to make the coffee
        """
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        """
        Returns a string representation of the coffee, including its name and ingredients.
        """
        return f"{self.name}: {self.ingredients}"

    @classmethod
    def from_menu(cls, option, menu):
        """
        Creates a Coffee object from the menu based on the selected option.

        :param option: The coffee option selected by the user (e.g., espresso, latte)
        :param menu: The menu dictionary containing all available coffee options
        :return: A Coffee object or None if the option is not found in the menu
        """
        if option in menu:
            return cls(option, menu[option]["ingredients"])
        else:
            return None  # Return None if the option is not available in the menu