from idlelib.pyparse import trans
from functions.switcher import switch
from functions.csv_functions.import_csv import import_csv_file
import pandas as pd
import datetime as dt


def main():

    df = pd.DataFrame()

    programShouldRun = True
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

        # check if the user wants to exit
        if userInput == "11":
            programShouldRun = False
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break

        # call the switch function to handle the menu option
        df = switch(userInput, df)


if __name__ == "__main__":
    main()
