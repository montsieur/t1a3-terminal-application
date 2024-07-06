from tabulate import tabulate # Import tabulate to create tables when displaying data
import datetime 

# Class for expense object(s)
class Expense:
    """

    This is the class that stores our expense information/attributes.

    """
    def __init__(self, name, date, amount, category) -> None:
        self.name = name
        self.date = date
        self.category = category
        self.amount = amount
        # self.payment_method = payment_method

# Class for Expense Tracker
class ExpenseTracker:

    # List to define categories for expenses
    expense_categories = [
        "Groceries", "Food", "Entertainment", "Rent",
        "Mortgage", "Utilities", "Shopping", "Misc"
    ]

    def __init__(self):
        # Initializes an empty list for monthly data for each instance
        self.monthly_data = []
        # Initializes budget to zero
        self.budget = 0.0 

    def set_budget(self, budget):
        self.budget = budget
        print(f"Budget is set to #{self.budget}")

