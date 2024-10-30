import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def select_csv_file() -> str:
    Tk().withdraw()
    file_path = askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
    )
    return file_path


def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = {"Date", "Category", "Description", "Amount"}
    if not required_columns.issubset(df.columns):
        print(
            f"Missing required columns. The CSV file must contain these columns: {required_columns}"
        )
        return pd.DataFrame()

    empty_columns = [col for col in required_columns if df[col].isnull().all()]
    if empty_columns:
        print(f"The following columns are completely empty: {empty_columns}")
        return pd.DataFrame()

    print("\n\nData imported successfully!")
    print(df.head())
    return df


def import_csv_file() -> pd.DataFrame:
    csv_file_path = select_csv_file()

    if csv_file_path:
        try:
            df = pd.read_csv(csv_file_path)
        except pd.errors.EmptyDataError:
            print("The selected CSV file is empty.")
            return pd.DataFrame()

        return validate_dataframe(df)
    else:
        print("No file selected.")
        return pd.DataFrame()
