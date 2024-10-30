from functions.data_visualization.visualization import (
    visualize_spending_trend,
    visualize_category_spending,
    visualize_percentage_distribution,
)


def get_visualization_choice():
    print("Choose a visualization option:")
    print("1. Monthly Spending Trend (Expenses)")
    print("2. Spending by Category (Expenses)")
    print("3. Percentage Distribution of Spending (Expenses)")

    choice = int(input("Enter your choice (1-3): "))
    return choice


def data_visualization_switch(transactions):
    # Get user choice
    user_input_value = get_visualization_choice()

    switcher = {
        1: lambda: visualize_spending_trend(transactions),
        2: lambda: visualize_category_spending(transactions),
        3: lambda: visualize_percentage_distribution(transactions),
    }

    # If invalid choice, prompt user to select again
    if user_input_value not in switcher:
        print("Invalid choice. Please select a number between 1 and 3.")
        return data_visualization_switch(transactions)
    else:
        func = switcher[user_input_value]
        func()
