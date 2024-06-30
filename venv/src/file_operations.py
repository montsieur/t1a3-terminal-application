# This file operation is to load and save CSV file of expenses from expense tracker.

import csv

def load_expenses(file_path)
    """
    Load monthly expenses from a CSV file
    
    """
    try:
        # Open File
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                #Append new expense
                expenses.append(row)
        return expenses
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    
    except Exception as e:
        print(f"An unexpected error has occured: {e}")
        return []
    
def save_expenses(file_path, expenses):
    try:
        # Open csv file
        with open(file_path, 'w') as file:
            write = csv.writer(file)
            writer.writerows(expenses)

    except PermissionError:
        print(f"Error: Permission denied to write file.")

    except Exception as e:
        print(f"An unexpected error has occured: {e}")