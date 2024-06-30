# from file_operations import load_expenses, save_expenses
from expense_tracker import ExpenseTracker, Expense, Budget

tracker = ExpenseTracker

budget_input = input("Enter your monthly budget: ")
tracker.set_budget(budget_input)

current_budget = tracker.view_budget()
print(f"Current monthly budget: {current_budget}")


