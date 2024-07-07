from expense import Expense # Import class attributes from Expense module
from tabulate import tabulate # Import tabulate to create tables when displaying data
import datetime # Import datetime to implement time and date within expense tracker
import csv # Import csv to handle csv files
import os # Import os to define and perform operating system operations
from rich import print # type: ignore # Import rich to implement color to text


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
                    print("[red3]Expense amount cannot be negative. Please enter a non-negative amount.[/red3]")
                else:
                    break

            # Calculate the total of existing expenses
            total_existing_expenses = sum(expense.amount for expense in self.monthly_data)
            # Update budget to reflect any existing expenses
            self.budget = budget - total_existing_expenses
            # Displays new total budget
            print(f"[green3]Budget is set to ${budget:.2f}.[/green3]")
            print(f"Your remaining budget is ${self.budget:.2f}.")
        
        # Error handling message for invalid value amount
        except ValueError:
            print("[red3]Invalid input. Please enter a valid number for the expense amount.[/red3]")
        # Error handling message for all other errors
        except Exception as e:
            print(f"[red3]An unexpected error has occured: {e}[/red3]")     

    # Clear any existing monthly data
    def clear_expenses(self):
        self.monthly_data = []

    # Add new expense into tracker
    def add_expense(self):
        try:
            # User inputs expense name
            while True:
                expense_name = input("Enter expense name: ")
                # Ensures input only contains letters of the alphabet without spaces
                if expense_name.replace(" ", "").isalpha():
                    break
                else:
                    # Error handling if input contains more then letters of alphabet
                    print("[red3]Invalid input. Please ensure expense name only contains letters.[/red3]")
            
            # User inputs expense amount 
            while True:
                expense_amount = float(input("Enter expense amount: "))
                if expense_amount < 0:
                    # Error handling if value is negative
                    print("[red3]Expense amount cannot be negative. Please enter a non-negative amount.[/red3]")
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
                    print("[red3]Invalid category number. Please try again.[/red3]")

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
                    print("[red3]Invalid payment method number. Please try again.[/red3]")           
            
            # Check if there enough budget remaining
            if expense_amount > self.budget:
                print("[red3]Warning, this expense exceeds your budget![/red3]")

            # Deduct the expense from the budget
            self.budget -= expense_amount

            # Create new object for expenses
            new_expense = Expense(name=expense_name, amount=expense_amount, date=expense_date, category=expense_category, payment_method=expense_payment_method, budget=self.budget)

            # Add expense into monthly data list
            self.monthly_data.append(new_expense)

            # Display message that expense entry has been recorded and remaining budget
            print("[green3]Expense has been recorded.[/green3]")
            print(f"Your remaining budget is ${self.budget:.2f}.")
            print(tabulate([[new_expense.name, f"{new_expense.amount:.2f}", new_expense.date, new_expense.category, new_expense.payment_method]], headers=["Name", "Amount", "Date", "Category", "Payment Method"], tablefmt="fancy_grid"))

        # Error handling message for invalid value amount
        except ValueError:
            print("[red3]Invalid input. Please enter a valid number for the expense amount.[/red3]")
        # Error handling message for all other errors
        except Exception as e:
            print(f"[red3]An unexpected error has occured: {e}[/red3]")
            
    # Remove an expense from the expense tracker monthly list
    def remove_expense(self):
        # If there is no expenses in the monthly data list
        if not self.monthly_data:
            print("[red3]No expenses recorded.[red3]")
            return
        
        # Displays current expenses in monthly data list
        self.view_expenses()
        
        try:
            # User input a number starting from 1 to remove an expense
            index = int(input("Enter index of the expense to remove (starting from 1): ")) - 1
            # Error handling if user input is less than 0
            if index < 0 or index >= len(self.monthly_data):
                raise IndexError("Index is not valid or does not exist. Please try again.")

            # Assigning attribute to remove_expense using pop python list method to remove item from index
            removed_expense = self.monthly_data.pop(index)

            print(f"[green3]Expense '{removed_expense.name}' removed successfully.[/green3]")

            # Deduct the expense from the budget
            self.budget += removed_expense.amount

            # Displays remaining expenses in monthly data list
            self.view_expenses()   

        # Error handling if user input is not an integer    
        except ValueError:
            print("[red3]Invalid input. Please enter a valid index number.[/red3]")
        # Error handling message for all other errors
        except Exception as e:
            print(f"[red3]An unexpected error has occured: {e}[/red3]")  

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
                print("[red3]No expenses recorded yet.[/red3]")

        # Error handling message for all other errors
        except Exception as e:
            print(f"[red3]An unexpected error has occured: {e}[/red3]")

    # Display total expenses if there are any in the monthly data list
    def total_expenses(self):
        try:
            if self.monthly_data:
                # Adds expenses from monthly data list
                total = sum(expense.amount for expense in self.monthly_data)
                # Displays total expenses and remaining budget
                print(f"[green3]Total expenses: ${total:.2f}[/green3]")
                print(f"Your remaining budget is ${self.budget:.2f}.")
            else:
                print("[red3]No expenses recorded yet.[/red3]")

        # Error handling message for all other errors
        except Exception as e:
            print(f"[red3]An unexpected error has occured: {e}[/red3]")

    # Method to export current expense data to csv file
    def save_expenses(self, filename):
        try:
            # Determines the path to the data folder from virtual environment folder
            venv_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            data_folder = os.path.join(venv_folder, 'data')

            # Saves CSV file to data folder
            file_path = os.path.join(data_folder, filename + ".csv")

            with open(file_path, 'w') as csvfile:
                writer = csv.writer(csvfile)
                # Writes headers for each value
                writer.writerow(["Name", "Amount", "Date", "Category", "Payment Method", "Budget"])
                # Writes values in attributes into monthly data list  
                for expense in self.monthly_data:
                    writer.writerow([expense.name, expense.amount, expense.date, expense.category, expense.payment_method, expense.budget])
            # Displays message when file is successfully saved
            print(f"[green3]Expenses saved to {file_path} successfully.[/green3]")

        # Error handling message when exporting csv file
        except Exception as e:
            print(f"[red3]Error saving expenses to '{file_path}': {e}[/red3]")

    # Method to import expense data from csv file
    def load_expenses(self, filename):
        try:
            # Determines the path to the data folder from virtual environment folder
            venv_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            data_folder = os.path.join(venv_folder, 'data')

            # Load CSV file to data folder
            file_path = os.path.join(data_folder, filename)

            # Reads CSV file chosen
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                # Initialize empty list for loaded expense list 
                loaded_expenses = []
                for row in reader:
                    amount = float(row['Amount'])
                    date = datetime.datetime.strptime(row['Date'], '%Y-%m-%d').date()
                    budget = float(row.get('Budget', 0.0)) 
                    expense = Expense(name=row['Name'], amount=amount, date=date, category=row['Category'], payment_method=row['Payment Method'], budget=budget)
                    # Creates object to append imported expense data
                    loaded_expenses.append(expense)
                
                # Clears any existing monthly_data before loading new monthly expense
                self.clear_expenses()

                # Extend self.monthly_data with loaded expenses
                self.monthly_data.extend(loaded_expenses)
                print(f"[green3]Successfully loaded {len(loaded_expenses)} expenses from {file_path}[/green3]")

                # Pulls and updates the budget to replace last recorded budget in the file
                if loaded_expenses:
                    self.budget = float(loaded_expenses[-1].budget)

        # Error handling when file name input is incorrect
        except FileNotFoundError:
            print(f"[red3]The file: {filename} cannot be found. Please enter the correct file name.[/red3]")
        # Error handling message for all other errors
        except Exception as e:
            print(f"[red3]An unexpected error has occurred: {e}[/red3]")

