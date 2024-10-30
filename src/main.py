from idlelib.pyparse import trans

from functions.switcher import switch
from functions.csv_functions.import_csv import import_csv_file
import pandas as pd
import datetime as dt

df = pd.DataFrame()
transactions = []



def main():
    programShouldRun = True

    global df, transactions


    while programShouldRun:
        print("\n\nPersonal Finance Tracker App")
        print("0.  Import a CSV file")
        print("1.  View All Transactions")
        print("2.  View Transactions by Date Range")
        print("3.  Add a Transaction")
        print("4.  Edit a Transaction")
        print("5.  Delete a Transaction")
        print("6.  Analyze Spending by Category")
        print("7.  Calculate Average Monthly Spending")
        print("8.  Show Top Spending Category")
        print("9.  Visualize Monthly Spending Trend")
        print("10. Save Transactions to CSV")
        print("11. Exit")

        # get user input
        userInput = input("Enter your choice: ")

        if userInput == "0":
            # Setting the dataframe
            df = import_csv_file()
            continue

        # check if the user wants to exit
        if userInput == "11":
            programShouldRun = False
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break

        # call the switch function to handle the menu option
        switch(userInput, df)

#data management


def correct_date_format(date_inputted): #to make sure the YYYY-MM-DD format is followed
    date_format = r"^\d{4}-\d{2}-\d{2}$"

def add_transaction():
    global transactions
    while True:
        date_inputted = input("Enter the date (YYYY-MM-DD):")
        if not correct_date_format(date_inputted):
            print("Please enter the right format YYYY-MM-DD!")
        try:
            date = dt.date.fromisoformat(date_inputted)
            break
        except ValueError:
            print("Please enter the right format YYYY-MM-DD!")
            continue

    category_inputted = input("Enter the category (e.g., Food, Rent:")

    description_inputted = input("Enter description:")

    amount_inputted = input("Enter the amount:")
    if amount_inputted.isdigit():
        amount = int(amount_inputted)
    else:
        print("Only able to enter numbers")
        return

    transaction = {"date" : date, "category" : category_inputted,
                   "description" : description_inputted,
                   "amount": amount_inputted}

    transactions.append(transaction)
    print("Transaction added succesfully!")

def view_transactions():
    global transactions
    start_date_input = input("Enter the start date (YYYY-MM-DD) :")
    end_date_input = input("Enter the end date (YYYY-MM-DD) :")
    if not (correct_date_format(start_date_input) and correct_date_format(end_date_input)):
        print("Enter date YYYY-MM-DD:")
        return
    for i, transaction in enumerate(transactions):
        print(f"{i}, {transaction}")


def remove_transaction():
    global transactions
    if not transactions:
        print("There no transactions to delete")
        return
    transaction_to_remove = input("Enter the index of the transaction to delete:")
    if transaction_to_remove.isdigit() and 0 <= int(transaction_to_remove) < len(transactions):
        transactions.pop(int(transaction_to_remove))
        print("Transaction deleted successfully!")
        return transactions
    else:
        print("Invalid index")
        return transactions






if __name__ == "__main__":
    main()
