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

    expense_categories = [
        "Groceries", "Food", "Entertainment", "Rent",
        "Mortgage", "Utilities", "Shopping", "Misc"
    ]

    def __init__(self):
        # Initializes an empty list for monthly data for each instance
        self.monthly_data = []
        # Initializes budget to zero
        self.budget = 0.0 
        # List to define categories for expenses

    # Set up budget for expense tracker
    def set_budget(self, budget):
        self.budget = budget
        print(f"Budget is set to ${self.budget:.2f}")

    # Add new expense into tracker
    def add_expense(self):
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        expense_date = datetime.date.today()
        
        # Display list of categories for user to choose
        print("Choose a category for the expense: ")
        for expense_type, category in enumerate(self.expense_categories, start=1):
            print(f"{expense_type}. {category}")
        
        category_index = int(input("Enter the number of the category (from 1 - 8): ")) - 1
        if category_index < 0 or category_index >= len(self.expense_categories):
            print("Invalid category number. Please try again.")
            return
        
        expense_category = self.expense_categories[category_index]

        # Create new object for expenses
        new_expense = Expense(name=expense_name, amount=expense_amount, date=expense_date, category=expense_category)

        # Add expense into monthly data list
        self.monthly_data.append(new_expense)

        # Display message that expense entry has been recorded
        print("Expense has been recorded.")
        print(tabulate([[new_expense.name, f"{new_expense.amount:.2f}", new_expense.date, new_expense.category]], headers=["Name", "Amount", "Date", "Category"], tablefmt="fancy_grid"))

    # Remove an expense from the expense tracker monthly list
    def remove_expense(self):
        # If there is no expenses in the monthly data list
        if not self.monthly_data:
            print("No expenses recorded.")
            return
        
        # Displays current expenses in monthly data list
        self.view_expenses()
        
        try:
            # User input a number starting from 1 to remove an expense
            index = int(input("Enter index of the expense to remove (starting from 1): ")) - 1
            # Error handling if user input is less than 0
            if index < 0 or index >= len(self.monthly_data):
                print("Invalid index. Please enter a valid index.")
                return

            # Assigning attribute to remove_expense using pop python list method to remove item from index
            removed_expense = self.monthly_data.pop(index)

            print(f"Expense '{removed_expense.name}' removed successfully.")

        # Error handling if user input is not an integer    
        except ValueError:
            print("Invalid input. Please enter a valid index number.")

        except Exception as e:
            print(f"An unexpected error has occured: {e}")

        # Displays remaining expenses in monthly data list
        self.view_expenses()        

    def view_expenses(self):
        try:
            # Display expenses if there are any in the monthly data list
            if self.monthly_data:
                expense_data = [[expense.name, f"{expense.amount:.2f}", expense.date] for expense in self.monthly_data]
                print(tabulate(expense_data, tablefmt="fancy_grid"))
            # Informs the user if no expenses has been recorded yet.
            else:
                print("No expenses recorded yet.")
        except Exception as e:
            print(f"An unexpected error has occured: {e}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.monthly_data)
        print(f"Total expenses: ${total:.2f}")
    

