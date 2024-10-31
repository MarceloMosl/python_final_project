import pandas as pd


# Function to check if the input is a DataFrame and not empty
def check_is_dataframe(transactions):
    # Check if transactions is a pandas DataFrame
    if not isinstance(transactions, pd.DataFrame):
        print(
            "Error: transactions is not a DataFrame. Please import the CSV file first."
        )
        return False

    # Check if the DataFrame is empty
    if transactions.empty:
        print(
            "Error: transactions DataFrame is empty. Please ensure the CSV file has data."
        )
        return False

    return True


# Function to check if the DataFrame has necessary columns
def check_required_columns(transactions, required_columns):
    # Check if all required columns are present in the transactions data columns
    # If any columns are missing, list them.
    missing_columns = [
        col for col in required_columns if col not in transactions.columns
    ]
    if missing_columns:
        print(
            f"Error: DataFrame missing required columns: {', '.join(missing_columns)}."
        )
        return False
    return True
