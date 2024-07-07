# Expense Tracker

## GitHub Repository
https://github.com/montsieur/t1a3-terminal-application

## Python Packages/Libraries

- csv
- datetime
- os
- tabulate
- rich

## Coding style guide

pep8

## Project Planning

### Trello
To plan for my project, I used Trello to create a check list ensuring the project meets all requirements of the assessment rubric.

My initial step was to implement the planning stage of the project before laying out the basic foundation on the application code for each module containing it's function and/or method. After laying out the foundation, I expanded each method and function one by one to ensure each function/method is functional with and without errors.

*With errors:*
I am able to determine the errors that will occur and expand specifically for those errors with the use of error handling. Once error has been determined, debugging process will proceed.

*Without errors:*
Ticking off checklist to proceed to the next function/method.

To finalize the project, it is required to compile and ensure application is executable with no errors.

Given the timeframe of the project, I had set the deadline to work around my schedule and ensure a final deadline.

***Below is the full check list and plan for my project.***

![trello_overallplan](docs/trello_planning.JPG)

### Flowchart

[ to add screenshots of flowchat of application ]

## Installation

[ instructions to install the application for use ]

## Modules

This application will contain 3 modules to run this application. This includes:

    - main.py
    - expense.py
    - expense_tracker.py

The expense.py stores the class Expense to contain attributes/values of stored data gained from user input/csv file.
![class_expense](docs/class_expense.JPG)

*More information on other modules below for their functions and methods.*

## Features

## Main Module

![main_module](docs/main.JPG)

Contained in `main.py`, initializes application using an instance and displays users main menu and sub menu whilst pulling methods and attributes from `expense_tracker.py`.

This is executed with:

![main_execute](docs/main_execute.JPG)

### Main Menu
Main menu will initialize once user starts up Expense Tracker Application.

    - Add new expense monthly tracker
    - Load expense monthly tracker
    - Instructions
    - Exiting Application

![main_menu](docs/main_menu.JPG)

Using `while True:`, contains a loop to have user choose from the following option using if, elif and else statements. 
`if:` and `elif:` to create statement for each choice. e.g:

`if choice == '1':` is the first initial statement of choice. If chosen by user, it will direct them to the sub-menu function
`elif choice == '2':`is the follow up statement of choice. If chosen by user, prompts user to enter file name. If True, direct user to sub-menu. If False, will print error handling message from load_expense method `print(f"The file: {filename} cannot be found. Please enter the correct file name.")`.

If `else:`, it breaks the loop as False and exits the application.
By having `choice = input("Enter your choice (1-4): ")`, this is to ensure user input will only contain input from 1, 2, 3 or 4.
If user input is not 1, 2, 3 or 4, application will notify user of error message to input a valid option; `print("Invalid choice. Please enter a number from 1 to 4.")` and redirects users to the main menu.

#### Add New Expense Monthly Tracker
Directs user to the sub menu if user proceeds to create a new tracker

    - Loads 'Sub Menu'

#### Load Expense Monthly Tracker
Prompts user to enter a file name to open up an existing monthly tracker

    - User input file name with file extension (.csv). e.g. august_2024.csv
    - Loads 'Sub Menu' once file is loaded


![method_load_expenses](docs/method_loadexpense.JPG)

#### Instructions
Displays a list of basic instructions for the user to read and learn more about how each function of the application works.
    
    - Shows brief explanation for each method/function in the main menu and sub menu

#### Exiting Application

    - Exits user from the application

### Sub Menu
Sub Menu will load and initialize after user has choosen 'Add new expense monthly tracker' or 'Load expense monthly tracker'
Once initialized, displays the sub menu to the user to select the following:

    - Set Budget
    - Add Expense
    - Remove an Expense
    - View Expenses
    - Total Expenses
    - Save/Export Expense File
    - Exit Application

![sub_menu](docs/sub_menu.JPG)

Using `while True:`, contains a loop to have user choose from the following option using if, elif and else statements. 
`if:` and `elif:` to create statement for each choice.
If `else:`, it breaks the loop as False and exits the application.
By having `choice = input("Enter your choice (1-7): ")`, this is to ensure user input will only contain input from 1, 2, 3, 4, 5, 6 or 7.
If user input is not 1, 2, 3, 4, 5, 6 or 7, application will notify user of error message to input a valid option; `print("Invalid choice. Please enter a number from 1 to 7.")` and redirects users to the main menu.

### Expense Tracker Module
Contained in `expense_tracker.py`, this is the class for the expense tracker module to define methods and inheriting attributes from the `class Expense` from `expense.py` module.

![class_expense_tracker](docs/class_expensetracker.JPG)

Within this class, it also stores attributes and information such as lists for expense type/category and payment methods, monthly data and sets budget attribute initial value to 0 if budget has not been set.

#### Set Budget
Prompts user to enter an amount to set their monthly budget.

    - Enter a budget amount
    - Displays budget amount set
    - Updates remaining budget [ if applicable for existing expenses ]

![set_budget](docs/method_set_budget.JPG)

#### Add Expense
Prompts user to follow the prompts to enter the details of their expense:

    - Name of the expense
    - Amount of the expense
    - Date of the expense
    - Category of the expense
    - Payment Method

User input for expense name:
![expense_name](docs/method_addexpense_name.JPG)

User input for expense amount:
![expense_amount](docs/method_addexpense_amount.JPG)

Expense date is automatically set depending on system's current clock time using `datetime` python package:
![expense_date](docs/method_addexpense_date.JPG)

User input for choice from category list:
![expense_category](docs/method_addexpense_category.JPG)

User input for choice from payment method list:
![expense_paymentmethod](docs/method_addexpense_paymentmethod.JPG)

User input for expense name:
![expense_result](docs/method_addexpense_after_input.JPG)

#### Remove an Expense
Shows user a list of existing expenses [ if applicable ]. Users will be able to choose from the following list to remove an expense, showing remaining expenses and remaining budget.

    - List all existing expenses
    - Choose from following expense list
    - Display remaining expenses and updated remaining budget

![remove_expense_invalid](docs/method_removeexpense_noexpense.JPG)

![remove_expense_valid](docs/method_removeexpense_withexpense.JPG)

#### View Expenses
Displays all expenses that has been recorded within the current monthly tracker loaded

    - view expense by month
        - allows users to select an entry by month
        - displays budget, remaining budget and expenses for the month
    - view expense by category
        - allows users to select an entry by category
        - displays budget, remaining budget and expenses for the selected category

![view_expenses](docs/method_viewexpense.JPG)

### Total Expenses
Displays the sum and total of all expenses within the current monthly tracker loaded

    - Display total amount in $ of expenses

![total_expenses](docs/method_totalexpense.JPG)

### Export expense file
Prompts user to save and name the file for their monthly tracker csv file

    - Allows user to export expense data to .csv file
    - User input file name without file extention. e.g. august_2024
    - Files are saved within application 'data' folder
    - Contains data of expense entries for month exported.

![save_expenses](docs/method_saveexpense.JPG)

### Exit Application

    - Directs users to return to main menu

## References

- https://peps.python.org/pep-0008/
- https://www.w3schools.io/file/python-csv-read-write/
- https://www.geeksforgeeks.org/os-path-module-python/?ref=lbp
- https://pypi.org/project/pyfiglet/
- https://pypi.org/project/tabulate/
- https://github.com/Textualize/rich
- https://rich.readthedocs.io/en/stable/appendix/colors.html