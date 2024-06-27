# Expense Tracker

## GitHub Repository
https://github.com/montsieur/t1a3-terminal-application

## Python Packages

csv
datetime

## Coding style guide

pep8

variables, loops, conditional control structures, error handling, functions, input and output, importing pythong packages and using functions from python packages.

## Project Planning

### Flowchart

[ to add screenshots of flowchat of application ]

### Trello

[ to add screenshots of project planning using Trello of application ]

## Installation

[ instructions to install the application for use ]

## Features

- ### Main Menu
    Displays the main menu to the user to select the following:

    - Manage Budget
    - Add Expense
    - Remove an Expense
    - View Expenses
    - Total Expenses
    - Export Expense File
    - Exit Application

- ### Manage Budget

    - View budget
        - Displays user's current budget (will show 0 if no entry of budget amount)
    - Update budget
        - Allows user's to update their budget (used also as an entry point for budget amount)

`remaining_budget = budget - get_total_expenses()`

- ### Add Expense

    - Amount of the expense
    - Date of the expense
    - Category of the expense
    - Name/Description of the expense
    - Payment Method

- ### Remove an Expense

    - Allows the user to remove an expense

- ### View Expenses

    - view expense by month
        - allows users to select an entry by month
        - displays budget, remaining budget and expenses for the month
    - view expense by category
        - allows users to select an entry by category
        - displays budget, remaining budget and expenses for the selected category

- ### Export expense file

    - Allows user to export expense data to .csv file
    - Files are saved on a user's desktop
    - Contains data of income and expense entries for month exported.

- ### Exit Application

    - Allows user's to close the application

## References

- https://peps.python.org/pep-0008/