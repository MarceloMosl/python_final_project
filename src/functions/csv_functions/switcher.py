from pandas import DataFrame
from functions.csv_functions.save_csv import save_csv_file


def csv_switch(df: DataFrame):
    save_csv_file(df)
