from data_cleaning import load_and_clean_data
from file_handling import save_cleaned_data, load_cleaned_data
from xception import DataCleaningError, FileHandlingError

try:
    cleaned_data = load_and_clean_data()
    save_cleaned_data(cleaned_data)
except DataCleaningError as e:
    print(e)

try:
    df = load_cleaned_data()
    confirmed = df['Confirmed'].sum()
    deaths = df['Deaths'].sum()
    recovered = df['Recovered'].sum()

    print(f"\nTotal Confirmed Cases: {confirmed}")
    print(f"Total Deaths: {deaths}")
    print(f"Total Recovered: {recovered}")

    highest = df.loc[df['Confirmed'].idxmax()]
    lowest = df.loc[df['Confirmed'].idxmin()]

    print(f"\nCountry with Highest Confirmed Cases: {highest['Country/Region']}")
    print(f"Confirmed Cases: {highest['Confirmed']}")
    
    print(f"\nCountry with Lowest Confirmed Cases: {lowest['Country/Region']}")
    print(f"Confirmed Cases: {lowest['Confirmed']}")

except FileHandlingError as e:
    print(e)
except Exception as e:
    print(f"Error is: {e}")

