from expense_tracker import ExpenseTracker # Import ExpenseTracker class from expense_tracker module
import pyfiglet # Import pyfiglet to convert text to ACSII art fonts

def main():
    # Creates instance for ExpenseTracker Class
    tracker = ExpenseTracker()

    # Creates header for application using pyfiglet
    styled_text = pyfiglet.figlet_format('Expense Tracker', font='doom')
    print(styled_text)


    while True:
    # Main Menu options
        print("\nExpense Tracker Menu:")
        print("1. Add new monthly tracker")
        print("2. Load monthly expense file")
        print("3. Instructions")
        print("4. Exit Application")
        choice = input("Enter your choice (1-4): ")

        # User input to select from menu
        if choice == '1':
            # Sub-menu for new expense tracker
            expense_tracker_sub_menu(tracker)

        elif choice == '2':
            filename = input("Enter the filename to load (e.g., expenses.csv): ")
            tracker.load_expenses(filename)
            # Automatically open the expense tracker submenu after loading expenses
            expense_tracker_sub_menu(tracker)

        elif choice == '3':
            pass

        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            # Error handling message for invalid input
            print("Invalid choice. Please enter a number from 1 to 4.")

def expense_tracker_sub_menu(tracker):    
    # Sub-menu options
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. Remove Expense")
        print("4. View Expenses")
        print("5. Total Expenses")
        print("6. Save Expenses to CSV")
        print("7. Return back to main menu")
        # User input to select from menu
        choice = input("Enter your choice (1-7): ")

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
            filename = input("Enter filename to save expenses: ")
            tracker.save_expenses(filename)

        # Return back to main menu
        elif choice == '7':
            print("Returning to main menu...")
            break

        else:
            # Error handling message for invalid input
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()