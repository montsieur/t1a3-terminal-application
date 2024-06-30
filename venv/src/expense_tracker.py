import datetime 

# Class for budget object(s)
class Budget:
    """

    This is the class that stores our budget information/attributes.

    """
    def __init__(self, budget_amount) -> None:
        self.budget_amount = budget_amount

# Class for expense object(s)
class Expense:
    """

    This is the class that stores our expense information/attributes.

    """
    def __init__(self, name, date, category, amount, payment_method) -> None:
        self.name = name
        self.date = date
        self.category = category
        self.amount = amount
        self.payment_method = payment_method

    # List to define categories for expenses
    # expense_category = [ Groceries, Food, Entertainment, Rent, Mortgage, Utilities, Shopping, Misc ]

# Class for Expense Tracker
class ExpenseTracker:
    def __init__(self):
        # Initializes an empty list for monthly data for each instance
        self.monthly_data = []
        # Initializes budget to zero
        self.budget = 0.0 

    def set_budget(self):
        while True:
            # Get user's monthly budget input
            budget_input = input("Enter your monthly budget: ")
            try:
                # Converts user's budget input as a float
                self.budget = float(budget_input)
                # Error handling message for invalid input
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception as e:
                print("Unexpected error has occured: {e}")

    def view_budget(self):
        # Retrieves budget user has set
        return self.budget