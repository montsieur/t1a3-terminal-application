import datetime 

# Class for budget object(s)
class Budget:
    """

    This is the class that stores our budget information/attributes.

    """
    def __init__(self, budget) -> None:
        self.budget = budget

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
    
    def add_expense(self):
        while True:
            try:
                expense_name = input("Enter the expense name: ")
                # Checks if user's input is only in alphabet
                if expense_name.isalpha():
                    break
            except Exception as e:
                print(f"An unexpected error occured: {e}")

        # Retrieves today's date and time of input
        expense_date = datetime.date.today()

        # User input from category list in expense_category
        expense_category = 0

        while True:
            try:
                expense_amount = float(input(f"Enter the expense amount: "))
                if expense_amount < 0:
                    print("Invalid input. Expense amount should be a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"An unexpected error occured: {e}")

        # User chooses from list of payment methods from payment_methods_category
        expense_payment_method = 0

        # Object to store expense details
        expense = (
            'name': expense_name,
            'date': expense_date,
            'amount': expense_amount,
            'category': expense_category,
            'payment_method': expense_payment_method
        )

        # Add expense entry to monthly_data list
        self.monthly_data.append(expense)

        print("Your expense has been added")
        # print(f"Your remaining balance is {self.budget - self.total_expense}")

    # def remove_expense(self):



    # def view_expense(self):


    # def total_expense(self):


      