import pandas as pd


def correct_date_format(date_inputted): #to make sure the YYYY-MM-DD format is followed
    date_format = r"^\d{4}-\d{2}-\d{2}$"


def view_all_transactions(transactions: pd.DataFrame):
    if not transactions:
        print("No transactions available")
        return
    print("\nAll Transactions:")
    for i, transaction in enumerate(transactions):
        print(f"{i}:, Date: {transaction["date"]}, Category: {transaction["category"]}, "
              f"Description: {transaction["description"]}, Amount: {transaction["amount"]}")


def view_transactions_by_date():
    global transactions
    start_date_input = input("Enter the start date (YYYY-MM-DD) :")
    end_date_input = input("Enter the end date (YYYY-MM-DD) :")
    if not (correct_date_format(start_date_input) and correct_date_format(end_date_input)):
        print("Enter date YYYY-MM-DD:")
        return
    for i, transaction in enumerate(transactions):
        print(f"{i}, {transaction}")

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


def edit_transaction():
    global transactions
    if not transactions:
        print("No transaction available to edit")
        return
    print("\nAvailable transactions to edit:")
    view_all_transactions()

    transaction_number = input("Enter the number of the transaction you would like to edit:")
    if transaction_number.isdigit() and 0 <= int(transaction_number) < len(transactions):
        number = int(transaction_number)
        transaction = transactions[number]

        print("\nCurrent transaction details:")
        print(f"Date: {transaction['date']}, Category: {transaction['category']}, "
              f"Description: {transaction['description']}, Amount: {transaction['amount']}")

        date_inputted = input("Enter the new date (YYYY-MM-DD) or press enter to keep the same:")
        if date_inputted and correct_date_format(date_inputted):
            transactions["date"] = dt.date.fromisoformat(date_inputted)

        category_inputted = input("Enter the new category or press enter to keep the same")
        if category_inputted:
            transaction["category"] = category_inputted

        description_inputted = input("Enter the new description or press enter to keep the same")
        if description_inputted:
            transaction["description"] = description_inputted

        amount_inputted = input("Enter the new amount or press enter to keep the same")
        if amount_inputted:
            if amount_inputted.isdigit():
                transaction["amount"] = int(amount_inputted)
            else:
                print("Invalid amount")

        print("Transaction updated successfully")
    else:
        print("Invalid Index")


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




