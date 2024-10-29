import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def select_csv_file():
    Tk().withdraw()
    file_path = askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
    )
    return file_path


def import_csv_file() -> pd.DataFrame:
    csv_file_path = select_csv_file()

    if csv_file_path:
        df = pd.read_csv(csv_file_path)
        print(f"Data imported successfully from {csv_file_path}")
        print(df.head())
        return df
    else:
        print("No file selected.")
        return pd.DataFrame()
