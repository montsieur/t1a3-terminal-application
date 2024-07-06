from file_operations import load_expenses, save_expenses
from expense import Expense
from tabulate import tabulate # Import tabulate to create tables when displaying data
import datetime # Import datetime to implement time and date within expense tracker

# Class for Expense Tracker
class ExpenseTracker:
    """

    This is the class that inherits 'Expense class' attributes and defines methods and functions of application

    """
    # List to define categories for expenses
    expense_categories = [
        "Groceries", "Food", "Entertainment", "Rent",
        "Mortgage", "Utilities", "Shopping", "Misc"
    ]
    # List to define categories for payment types
    payment_method_categories = [
        "Cash", "Credit Card", "Debit Card"
    ]

    def __init__(self):
        # Initializes an empty list for monthly data for each instance
        self.monthly_data = []
        # Initializes budget to zero
        self.budget = 0.0 

    # Set up budget for expense tracker
    def set_budget(self):
        try:
            while True:
                # User inputs budget amount
                budget = float(input("Enter your budget amount: "))
                if budget < 0:
                    # Error handling if value is negative
                    print("Expense amount cannot be negative. Please enter a non-negative amount.")
                else:
                    break
            # Calculate the total of existing expenses
            total_existing_expenses = sum(expense.amount for expense in self.monthly_data)
            # Update budget to reflect any existing expenses
            self.budget = budget - total_existing_expenses
            print(f"Budget is set to ${budget:.2f}")
        
        # Error handling message for invalid value amount
        except ValueError:
            print("Invalid input. Please enter a valid number for the expense amount.")
        # Error handling message for all other errors
        except Exception as e:
            print(f"An unexpected error has occured: {e}")    


    # Add new expense into tracker
    def add_expense(self):
        try:
            # User inputs expense name
            while True:
                expense_name = input("Enter expense name: ")
                # Ensures input only contains letters of the alphabet without spaces
                if expense_name.replace(" ", "").isalpha():
                    break
                # Error handling if input contains more then letters of alphabet
                else:
                    print("Invalid input. Please ensure expense name only contains letters.")
            
            # User inputs expense amount 
            while True:
                expense_amount = float(input("Enter expense amount: "))
                if expense_amount < 0:
                    print("Expense amount cannot be negative. Please enter a non-negative amount.")
                else:
                    break

            # Automatically sets time to today's date and time
            expense_date = datetime.date.today()
            
            # User chooses from list of inputs for expense category
            print("Choose a category for the expense: ")
            # Creates and displays a tuple for category list numbering them from 1 - 8
            for expense_type, category in enumerate(self.expense_categories, start=1):
                print(f"{expense_type}. {category}")
            
            while True:
                category_index = int(input("Enter the number of the category (from 1 - 8): ")) - 1
                if 0 <= category_index < len(self.expense_categories):
                    expense_category = self.expense_categories[category_index]
                    break
                else:
                    # Error handling for invalid index input
                    print("Invalid category number. Please try again.")

            # User chooses from list of inputs for payment method
            print("Choose a payment method for the expense: ")
            # Creates and displays a tuple for category list numbering them from 1 - 3
            for payment_type, payment_method in enumerate(self.payment_method_categories, start=1):
                print(f"{payment_type}. {payment_method}")
            
            while True:
                payment_method_index = int(input("Enter the number of the category (from 1 - 3): ")) - 1
                if 0 <= payment_method_index < len(self.payment_method_categories):
                    expense_payment_method = self.payment_method_categories[payment_method_index]
                    break
                else:
                    # Error handling for invalid index input
                    print("Invalid payment method number. Please try again.")           
            
            # Check if there enough budget remaining
            if expense_amount > self.budget:
                print("Warning, this expense exceeds your budget!")

            # Deduct the expense from the budget
            self.budget -= expense_amount

            # Create new object for expenses
            new_expense = Expense(name=expense_name, amount=expense_amount, date=expense_date, category=expense_category, payment_method=expense_payment_method)

            # Add expense into monthly data list
            self.monthly_data.append(new_expense)

            # Display message that expense entry has been recorded and remaining budget
            print("Expense has been recorded.")
            print(f"Your remaining budget is ${self.budget:.2f}.")
            print(tabulate([[new_expense.name, f"{new_expense.amount:.2f}", new_expense.date, new_expense.category, new_expense.payment_method]], headers=["Name", "Amount", "Date", "Category", "Payment Method"], tablefmt="fancy_grid"))

        # Error handling message for invalid value amount
        except ValueError:
            print("Invalid input. Please enter a valid number for the expense amount.")
        # Error handling message for all other errors
        except Exception as e:
            print(f"An unexpected error has occured: {e}")
            
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

            # Deduct the expense from the budget
            self.budget += removed_expense.amount

            # Displays remaining expenses in monthly data list
            self.view_expenses()   

        # Error handling if user input is not an integer    
        except ValueError:
            print("Invalid input. Please enter a valid index number.")
        # Error handling message for all other errors
        except Exception as e:
            print(f"An unexpected error has occured: {e}")  

    # Display expenses if there are any in the monthly data list
    def view_expenses(self):
        try:
            if self.monthly_data:
                expense_data = [[expense.name, f"{expense.amount:.2f}", expense.date, expense.category, expense.payment_method] for expense in self.monthly_data]
                # Displays table of expenses  and remaining budget
                print(f"Your remaining budget is ${self.budget:.2f}.")
                print(tabulate(expense_data, headers=["Name", "Amount", "Date", "Category", "Payment Method"], tablefmt="fancy_grid"))
            # Informs the user if no expenses has been recorded yet.
            else:
                print("No expenses recorded yet.")

        # Error handling message for all other errors
        except Exception as e:
            print(f"An unexpected error has occured: {e}")

    # Display total expenses if there are any in the monthly data list
    def total_expenses(self):
        try:
            if self.monthly_data:
                # Adds expenses from monthly data list
                total = sum(expense.amount for expense in self.monthly_data)
                # Displays total expenses and remaining budget
                print(f"Your remaining budget is ${self.budget:.2f}.")
                print(f"Total expenses: ${total:.2f}")
            else:
                print("No expenses recorded yet.")

        # Error handling message for all other errors
        except Exception as e:
            print(f"An unexpected error has occured: {e}")
    

