import pandas as pd
import datetime as dt
import re


def correct_date_format(
    date_inputted,
):
    date_format = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(date_format, date_inputted))


def view_all_transactions(transactions: pd.DataFrame):
    if transactions.empty:
        print("No transactions available")
        return
    print("\nAll Transactions:")
    for i, transaction in transactions.iterrows():
        print(
            f"{i}:, Date: {transaction["Date"]}, Category: {transaction["Category"]}, "
            f"Description: {transaction["Description"]}, Amount: {transaction["Amount"]}"
        )


def view_transactions_by_date(transactions: pd.DataFrame):
    start_date_input = input("Enter the start date (YYYY-MM-DD): ")
    end_date_input = input("Enter the end date (YYYY-MM-DD): ")

    if not (
        correct_date_format(start_date_input) or correct_date_format(end_date_input)
    ):
        view_all_transactions(transactions)
        return

    filter_date = transactions[
        (transactions["Date"] >= start_date_input)
        & (transactions["Date"] <= end_date_input)
    ]

    if filter_date.empty:
        print("No transactions found")
    else:
        print("\nTransactions found:")
        view_all_transactions(filter_date)


def add_transaction(transactions: pd.DataFrame):
    date_inputted = input("Enter the date (YYYY-MM-DD):")

    while not correct_date_format(date_inputted):
        print("Please enter the right format YYYY-MM-DD!")
        date_inputted = input("Enter the date (YYYY-MM-DD): ")

    category_inputted = input("Enter the category (e.g., Food, Rent): ")

    description_inputted = input("Enter description: ")

    while True:
        amount_inputted = input("Enter the amount:")
        try:
            amount_inputted = float(amount_inputted)
            break
        except ValueError:
            print("Please enter only numbers")

    type_inputted = input(
        "Select the type of the transaction: (Expense or Income): "
    ).lower()

    while type_inputted not in ["expense", "income"]:
        type_inputted = input(
            "Select the type of the transaction: (Expense or Income): "
        ).lower()

    transaction = pd.DataFrame(
        {
            "Date": [date_inputted],
            "Category": [category_inputted],
            "Description": [description_inputted],
            "Amount": [amount_inputted],
            "Type": [type_inputted.capitalize()],
        }
    )

    print("Transaction added succesfully!")
    return pd.concat([transactions, transaction], ignore_index=True)


import pandas as pd
from datetime import datetime as dt


def edit_transaction(transactions: pd.DataFrame):
    if transactions.empty:
        print("No transactions available to edit.")
        return transactions

    print("\nAvailable transactions to edit:")
    view_all_transactions(transactions)

    transaction_number = input(
        "Enter the index of the transaction you would like to edit: "
    )

    if transaction_number.isdigit() and 0 <= int(transaction_number) < len(
        transactions
    ):
        number = int(transaction_number)

        print("\nCurrent transaction details:")
        print(
            f"Date: {transactions.at[number, 'Date']}, "
            f"Category: {transactions.at[number, 'Category']}, "
            f"Description: {transactions.at[number, 'Description']}, "
            f"Amount: {transactions.at[number, 'Amount']}"
        )

        date_inputted = input(
            "Enter the new date (YYYY-MM-DD) or press enter to keep the same: "
        )
        if date_inputted and correct_date_format(date_inputted):
            transactions.at[number, "Date"] = date_inputted

        category_inputted = input(
            "Enter the new category or press enter to keep the same: "
        )
        if category_inputted:
            transactions.at[number, "Category"] = category_inputted

        description_inputted = input(
            "Enter the new description or press enter to keep the same: "
        )
        if description_inputted:
            transactions.at[number, "Description"] = description_inputted

        amount_inputted = input(
            "Enter the new amount or press enter to keep the same: "
        )
        if amount_inputted:
            try:
                transactions.at[number, "Amount"] = float(amount_inputted)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        print("Transaction updated successfully!")
    else:
        print("Invalid index.")

    return transactions


def remove_transaction(transactions: pd.DataFrame):
    if transactions.empty:
        print("There are no transactions to delete.")
        return transactions

    try:
        transaction_to_remove = int(
            input("Enter the index of the transaction to delete: ")
        )

        if 0 <= transaction_to_remove < len(transactions):
            transactions = transactions.drop(index=transaction_to_remove).reset_index(
                drop=True
            )
            print("Transaction deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a numeric index.")

    return transactions
