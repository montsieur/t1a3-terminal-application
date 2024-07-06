from expense_tracker import ExpenseTracker

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. Remove Expense")
        print("4. View Expenses")
        print("5. Total Expenses")
        print("6. Save Expenses to CSV")
        print("7. Load Expenses from CSV")
        print("8. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            budget = float(input("Enter your budget for this period: $"))

        elif choice == '2':
            amount = float(input("Enter amount spent: $"))
            category = int(input("Enter category number: ")) - 1
            name = input("Enter name of expense: ")
            date = input("Enter date of expense (MM/DD/YYYY): ")
            payment_method = input("Enter payment method: ")

        elif choice == '3':
            index = int(input("Enter index of expense to remove: ")) - 1

        elif choice == '4':
            pass

        elif choice == '5':
            pass

        elif choice == '6':
            filename = input("Enter filename to save expenses (e.g., expenses.csv): ")

        elif choice == '7':
            filename = input("Enter filename to load expenses from (e.g., expenses.csv): ")

        elif choice == '8':
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")