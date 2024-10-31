from functions.spending_analysis.spending_analysis import (
    analyze_spending_by_category,
    calculate_average_monthly_spending,
    show_top_spending_category,
)


def spending_analysis_switch(value, transactions):
    switcher = {
        "6": lambda: analyze_spending_by_category(transactions),
        "7": lambda: calculate_average_monthly_spending(transactions),
        "8": lambda: show_top_spending_category(transactions),
    }

    # Default action for invalid value
    func = switcher.get(
        value,
        lambda: print(
            "Invalid choice. Please select a valid option for Spending Analysis."
        ),
    )

    # Call the appropriate function
    func()
