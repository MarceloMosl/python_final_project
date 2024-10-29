from functions.csv_functions.switcher import csv_switch
from functions.data_management.switcher import data_management_switch
from functions.data_vizualization.switcher import data_vizualization_switch
from functions.spending_analysis.switcher import spending_analysis_swticher


def switch(value):
    switcher = {
        "1": lambda: csv_switch(value),  # CSV file related functions
        "2": lambda: data_management_switch(value),  # Data-Management related functions
        "3": lambda: data_vizualization_switch(
            value
        ),  # Data-Vizualization related functions
        "4": lambda: spending_analysis_swticher(
            value
        ),  # Spending Analysis related functions
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose a valid option.")
    )()
