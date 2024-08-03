import pandas as pd
from exceptions import FileHandlingError

def save_cleaned_data(df, filename='clean_covid_data.csv'):
    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        raise FileHandlingError(f"Error saving file: {e}")

def load_cleaned_data(filename='clean_covid_data.csv'):
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        raise FileHandlingError(f"Error loading file: {e}")
