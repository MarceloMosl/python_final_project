from functions.csv_functions.switcher import csv_switch
from functions.data_management.switcher import data_management_switch
from functions.data_vizualization.switcher import data_vizualization_switch
from functions.spending_analysis.switcher import spending_analysis_swticher


def switch(value):
    switcher = {
        "0": lambda: csv_switch(value),  # Import a CSV file
        "1": lambda: data_management_switch(value),  # View All Transactions
        "2": lambda: data_management_switch(value),  # View Transactions by Date Range
        "3": lambda: data_management_switch(value),  # Add a Transaction
        "4": lambda: data_management_switch(value),  # Edit a Transaction
        "5": lambda: data_management_switch(value),  # Delete a Transaction
        "6": lambda: spending_analysis_swticher(value),  # Analyze Spending by Category
        "7": lambda: spending_analysis_swticher(
            value
        ),  # Calculate Average Monthly Spending
        "8": lambda: spending_analysis_swticher(value),  # Show Top Spending Category
        "9": lambda: data_vizualization_switch(
            value
        ),  # Visualize Monthly Spending Trend
        "10": lambda: csv_switch(value),  # Save Transactions to CSV
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose a valid option.")
    )()
