from tabulate import tabulate # Import tabulate to create tables when displaying data
import datetime 

# Class for expense object(s)
class Expense:
    """

    This is the class that stores our expense information/attributes.

    """
    def __init__(self, name, date, amount) -> None:
        self.name = name
        self.date = date
        # self.category = category
        self.amount = amount
        # self.payment_method = payment_method

# Class for Expense Tracker
class ExpenseTracker:

    def __init__(self):
        # Initializes an empty list for monthly data for each instance
        self.monthly_data = []
        # Initializes budget to zero
        self.budget = 0.0 
        # List to define categories for expenses
        # expense_categories = [
        #     "Groceries", "Food", "Entertainment", "Rent",
        #     "Mortgage", "Utilities", "Shopping", "Misc"
        # ]

    # Set up budget for expense tracker
    def set_budget(self, budget):
        self.budget = budget
        print(f"Budget is set to ${self.budget:.2f}")

    # Add new expense into tracker
    def add_expense(self):
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        expense_date = datetime.date.today()

        # Create new object for expenses
        new_expense = Expense(name=expense_name, amount=expense_amount, date=expense_date)

        # Display message that expense entry has been recorded
        print("Expense has been recorded.")
        print(tabulate([[new_expense.name, f"{new_expense.amount:.2f}", new_expense.date]], headers=["Name", "Amount", "Date"], tablefmt="fancy_grid"))



