import pandas as pd
from tkinter import Tk, simpledialog
from tkinter.filedialog import askdirectory


def select_folder_and_filename():
    Tk().withdraw()

    folder_path = askdirectory(title="Select a folder")

    if folder_path:
        filename = simpledialog.askstring(
            "Input", "Enter the filename (without extension .csv):"
        )

        if filename:
            file_path = f"{folder_path}/{filename}.csv"
            return file_path

    return None


def save_csv_file(df: pd.DataFrame):
    if df.empty:
        print("Please Import a CSV file before saving a new one. :D")
        return

    filename = select_folder_and_filename()
    if filename == None:
        return

    df.to_csv(filename)
    print("File saved succesfully!")
