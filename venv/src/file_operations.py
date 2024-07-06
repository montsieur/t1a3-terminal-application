import csv
import datetime

from expense import Expense  # Assuming Expense class is defined in expense.py

def load_expenses(filename):
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            expenses = []
            for row in reader:
                name = row['Name']
                date = datetime.datetime.strptime(row['Date'], '%Y-%m-%d').date()
                category = row['Category']
                amount = float(row['Amount'])
                payment_method = row['Payment Method']
                
                new_expense = Expense(name, date, amount, category, payment_method)
                expenses.append(new_expense)
            
            print("Expenses loaded successfully from CSV.")
            return expenses

    except FileNotFoundError:
        print(f"File '{filename}' not found. No expenses loaded.")
        return []

    except Exception as e:
        print(f"An unexpected error occurred while loading expenses: {e}")
        return []

def save_expenses(expenses, filename):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Date', 'Amount', 'Category', 'Payment Method'])
            for expense in expenses:
                writer.writerow([expense.name, expense.date.strftime('%Y-%m-%d'), expense.amount, expense.category, expense.payment_method])
            
            print("Expenses saved successfully to CSV.")

    except Exception as e:
        print(f"An unexpected error occurred while saving expenses: {e}")
