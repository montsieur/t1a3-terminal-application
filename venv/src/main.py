from expense_tracker import ExpenseTracker # Import ExpenseTracker class from expense_tracker module
import pyfiglet # Import pyfiglet to convert text to ACSII art fonts

def main():
    # Creates instance for ExpenseTracker Class
    tracker = ExpenseTracker()

    # Creates header for application using pyfiglet
    styled_text = pyfiglet.figlet_format('Expense Tracker', font='doom')
    print(styled_text)

    # Main Menu options
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
        # User input to select from menu
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            tracker.set_budget()

        elif choice == '2':
            tracker.add_expense()

        elif choice == '3':
            tracker.remove_expense()

        elif choice == '4':
            tracker.view_expenses()

        elif choice == '5':
            tracker.total_expenses()

        elif choice == '6':
            pass

        elif choice == '7':
            pass
        # To exit the application
        elif choice == '8':
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            # Error handling message for invalid input
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()