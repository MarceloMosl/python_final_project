from csv_switcher import csv_switch
from data_management import data_management_switcher
from data_vizualization import data_vizualization_switcher
from spending_analysis import spending_analysis_switcher


def switch(value):
    switcher = {
        "1": lambda: csv_switch(),  # CSV file related functions
        "2": lambda: data_management_switcher(),  # Data-Management related functions
        "3": lambda: data_vizualization_switcher(),  # Data-Vizualization related functions
        "4": lambda: spending_analysis_switcher(),  # Spending Analysis related functions
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose a valid option.")
    )()
