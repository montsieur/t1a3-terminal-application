from expense_tracker import ExpenseTracker

def main():

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

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            budget = float(input("Enter your budget amount: "))
            tracker.set_budget(budget)

        elif choice == '2':
            tracker.add_expense()

        elif choice == '3':
            tracker.remove_expense()

        elif choice == '4':
            pass

        elif choice == '5':
            pass

        elif choice == '6':
            pass

        elif choice == '7':
            pass

        elif choice == '8':
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            # Error handling message for invalid input
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()