from datetime import datetime 

def add_expense(expenses , amount , category , note):  # Creates a new expense dictionary with current date/time and appends it to the existing list.
    expense = {
        "amount" : amount , 
        "category" : category ,
        "note" : note , 
        "date" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    return expenses

def list_expenses(expenses):
    for idx , exp in enumerate(expenses , 1): # enumerate : adds a counter to an iterable
        print(f"{idx}. [{exp['date']}] ₹{exp['amount']} - {exp['category']} ({exp['note']})")


def delete_expense(expenses , index): # index based deleting
    if 0 <= index < len(expenses) :   # Removes the expense at the given index if it's valid
        removed = expenses.pop(index) 
        print(f"Removed: ₹{removed['amount']} - {removed['category']}")
    else :
        print("Invalid index")
    return expenses
              
