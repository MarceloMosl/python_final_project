import pandas as pd
import matplotlib.pyplot as plt


# Monthly Spending Trend (Line Chart)
def visualize_spending_trend(transactions):
    # Ensure the 'Date' column is in datetime format
    transactions["Date"] = pd.to_datetime(transactions["Date"])

    # Filter only 'Expense' entries
    expense_transactions = transactions[transactions["Type"] == "Expense"]

    # Group by Month and calculate the total spending per month
    monthly_spending = expense_transactions.groupby(
        expense_transactions["Date"].dt.to_period("M")
    )["Amount"].sum()

    # Check if we have more than one data point
    if len(monthly_spending) > 1:
        # Plot the monthly spending trend as a line chart
        monthly_spending.plot(kind="line", marker="o", title="Monthly Spending Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Spending")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print(
            "Not enough data to display a trend. Add more transactions across different months."
        )


# Spending by Category (Bar Chart)
def visualize_category_spending(transactions):
    # Group by Category and sum up the 'Amount' for each category (only 'Expense')
    category_spending = (
        transactions[transactions["Type"] == "Expense"]
        .groupby("Category")["Amount"]
        .sum()
    )

    # Plot the spending by category as a bar chart
    category_spending.plot(kind="bar", title="Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Spending")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Percentage Distribution of Spending (Pie Chart)
def visualize_percentage_distribution(transactions):
    # Group by Category and sum up the 'Amount' for each category (only 'Expense')
    category_spending = (
        transactions[transactions["Type"] == "Expense"]
        .groupby("Category")["Amount"]
        .sum()
    )

    # Plot the spending distribution as a pie chart
    category_spending.plot(
        kind="pie", autopct="%1.1f%%", title="Percentage Distribution of Spending"
    )
    plt.ylabel("")  # Hides the y-label in the pie chart for a cleaner look
    plt.show()
