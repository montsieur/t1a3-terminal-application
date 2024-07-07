from expense_tracker import ExpenseTracker # Import ExpenseTracker class from expense_tracker module
import pyfiglet # Import pyfiglet to convert text to ACSII art fonts
from rich import print

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
            # If data is found in file, loads sub-menu
            if tracker.monthly_data:
                expense_tracker_sub_menu(tracker)

        elif choice == '3':
            # Display welcome message and brief instructions on how to use the application
            print("Welcome to your personal 'Expense Tracker'!\n")
            print("To help you use this application, here are some simple instructions:\n")
            print("1. To start tracking a new month, select 'Option 1'.")
            print("2. To load an existing expense tracker file, select 'Option 2'. You will be prompted to enter the csv file name.")
            print("- Note: Please ensure file is in the /data folder")
            print("3. To exit the Expense Tracker application, select 'Option 4'.\n")
            print("Sub-Menu options after choosing to create a new monthly tracker or loading an existing tracker:")
            print("1. Set your budget for the month using the 'Set Budget' option.")
            print("- To update your budget, repeat previous step to update your new budget.")
            print("2. Enter your expenses if there are no expenses recorded using the 'Add Expense' option.")
            print("3. Delete expense entries using the 'Remove Expense' option.")
            print("4. View all of your expenses within the month using the 'View Expenses' option.")
            print("5. View total expenses within the month using the 'Total Expenses' option.")
            print("6. Export your monthly expenses into a csv file using 'Save Expenses' option.")
            print("- Note: The file will be saved into the data folder.")
            print("7. To return back to menu, select 'Option 7'.")
            print("Thank you for using this application.")

        elif choice == '4':
            print("Exiting the Expense Tracker. See you next time!")
            break
        else:
            # Error handling message for invalid input
            print("[red3]Invalid choice. Please enter a number from 1 to 4.[/red3]")

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