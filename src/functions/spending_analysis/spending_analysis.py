import pandas as pd
from functions.common import check_is_dataframe, check_required_columns


def analyze_spending_by_category(transactions):
    # Ensure transactions is a DataFrame
    if not check_is_dataframe(transactions):
        return

    # Ensure the necessary columns are present
    if not check_required_columns(transactions, ["Category", "Type", "Amount"]):
        return

    # Group by Category and sum up the 'Amount' for each category (only 'Expense')
    category_spending = (
        transactions[transactions["Type"] == "Expense"]
        .groupby("Category")["Amount"]
        .sum()
    )

    # Display the total spending for each category
    print("--- Total Spending by Category ---")
    print(category_spending)


def calculate_average_monthly_spending(transactions):
    # Ensure transactions is a DataFrame
    if not check_is_dataframe(transactions):
        return

    # Ensure the necessary columns are present
    if not check_required_columns(transactions, ["Date", "Type", "Amount"]):
        return

    # Ensure the 'Date' column is in datetime format
    transactions["Date"] = pd.to_datetime(transactions["Date"])

    # Filter only 'Expense' entries
    expense_transactions = transactions[transactions["Type"] == "Expense"]

    # Group by Month and calculate total spending per month
    monthly_spending = expense_transactions.groupby(
        expense_transactions["Date"].dt.to_period("M")
    )["Amount"].sum()

    # Calculate the average monthly spending
    if not monthly_spending.empty:
        average_spending = monthly_spending.mean()
        print(f"--- Average Monthly Spending ---\n{average_spending:.2f}")
    else:
        print("No expenses recorded.")


def show_top_spending_category(transactions):
    # Ensure transactions is a DataFrame
    if not check_is_dataframe(transactions):
        return

    # Ensure the necessary columns are present
    if not check_required_columns(transactions, ["Category", "Type", "Amount"]):
        return

    # Group by Category and sum up the 'Amount' for each category (only 'Expense')
    category_spending = (
        transactions[transactions["Type"] == "Expense"]
        .groupby("Category")["Amount"]
        .sum()
    )

    # Remove NaN values from the category_spending Series
    category_spending = category_spending.dropna()

    # Check if there are still any valid spending data after removing NaN
    if category_spending.empty:
        print("No valid expenses recorded. All values are NaN or missing.")
        return

    # Find the maximum spending amount
    top_amount = category_spending.max()

    # Find all categories that have the maximum spending and get the category names as a list
    top_categories = category_spending[category_spending == top_amount].index.tolist()

    if len(top_categories) == 1:
        # If there is only one top category
        print(
            f"--- Top Spending Category ---\n{top_categories[0]} with {top_amount:.2f} total spending."
        )
    else:
        # If there are multiple categories with the same top spending amount
        categories_str = ", ".join(top_categories)
        print(
            f"--- Top Spending Categories ---\n{categories_str} with {top_amount:.2f} total spending each."
        )
