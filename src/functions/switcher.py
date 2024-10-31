from functions.csv_functions.import_csv import import_csv_file
from functions.csv_functions.switcher import csv_switch
from functions.data_management.switcher import data_management_switch
from functions.data_visualization.switcher import data_visualization_switch
from functions.spending_analysis.switcher import spending_analysis_switch


def switch(value, df):

    switcher = {
        "0": lambda: import_csv_file(),  # Import a CSV file
        "1": lambda: data_management_switch(value, df),  # View All Transactions
        "2": lambda: data_management_switch(
            value, df
        ),  # View Transactions by Date Range
        "3": lambda: data_management_switch(value, df),  # Add a Transaction
        "4": lambda: data_management_switch(value, df),  # Edit a Transaction
        "5": lambda: data_management_switch(value, df),  # Delete a Transaction
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
    updated_df = switcher.get(
        value, lambda: print("Invalid option, please choose a valid option.")
    )()
    return updated_df if updated_df is not None else df
