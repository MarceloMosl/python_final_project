from functions.csv_functions.switcher import csv_switch
from functions.data_management.switcher import data_management_switch
from functions.data_visualization.switcher import data_visualization_switch
from functions.spending_analysis.switcher import spending_analysis_switch


def switch(value, df):
    switcher = {
        "1": lambda: data_management_switch(value),  # View All Transactions
        "2": lambda: data_management_switch(value),  # View Transactions by Date Range
        "3": lambda: data_management_switch(value),  # Add a Transaction
        "4": lambda: data_management_switch(value),  # Edit a Transaction
        "5": lambda: data_management_switch(value),  # Delete a Transaction
        "6": lambda: spending_analysis_switch(
            value, df
        ),  # Analyze Spending by Category
        "7": lambda: spending_analysis_switch(
            value, df
        ),  # Calculate Average Monthly Spending
        "8": lambda: spending_analysis_switch(value, df),  # Show Top Spending Category
        "9": lambda: data_visualization_switch(df),  # Visualize Monthly Spending Trend
        "10": lambda: csv_switch(df),  # Save Transactions to CSV
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose a valid option.")
    )()
