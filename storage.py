import json # is used to read/write data in JSON format.
import os # helps check if the file exists.

DATA_FILE = "data/expenses.json" 


def load_expenses() :
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0 : # Loads data from expenses.json.
        return []                     # if the data doesn't exist , returns the empty list 
    with open(DATA_FILE, "r") as f:
        return json.load(f) 


def save_expenses(expenses): # Saves the current list of expenses to expenses.json.
    with open(DATA_FILE, "w") as f:
        json.dump(expenses , f , indent = 4) # ident = 4 , is to make it presentable 