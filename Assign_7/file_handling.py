import pandas as pd
from xception import FileHandlingError

def save_cleaned_data(df, filename='clean_covid_data.csv'):
    try:
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        raise FileHandlingError(f"Error: {e}")

def load_cleaned_data(filename='clean_covid_data.csv'):
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        raise FileHandlingError(f"Error: {e}")
