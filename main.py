# Imports functions from the other modules to keep this file clean and focused on CLI.
from tracker import add_expense, list_expenses, delete_expense
from storage import load_expenses, save_expenses
from visualiser import show_spending_by_category
from utils import validate_amount

def main():
    expenses = load_expenses()  

    while True: 
        print("\n----- Expense Tracker ------")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Spending by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':  # Option 1: Add Expense
            amt = None
            while amt is None :
                amt = validate_amount(input("Amount: "))
                if amt is None :
                    print("Please enter a valid amount")
            cat = input("Category: ")
            note = input("Note: ")
            expenses = add_expense(expenses, amt, cat, note)
            save_expenses(expenses)
            print("Expense Added!")

        elif choice == '2':  # Option 2: View Expenses
            list_expenses(expenses)

        elif choice == '3':  # Option 3: Delete Expense
            list_expenses(expenses)
            index = int(input("Enter an index to delete: ")) - 1  # -1 for 0-based index
            expenses = delete_expense(expenses, index)
            save_expenses(expenses)

        elif choice == '4' :
            show_spending_by_category(expenses)

        elif choice == '5':  # Option 4: Exit
            break

        else:  # Invalid input
            print("Invalid choice!")

if __name__ == "__main__":
    main()
