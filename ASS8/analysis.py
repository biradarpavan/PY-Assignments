from data_cleaning import load_and_clean_data
from file_handling import save_cleaned_data
from visualization import plot_total_cases, plot_top_countries, plot_daily_cases

def main():
    try:
        cleaned_data = load_and_clean_data()
        save_cleaned_data(cleaned_data)
        
        plot_total_cases(cleaned_data)
        plot_top_countries(cleaned_data)
        plot_daily_cases(cleaned_data)
        
        print("Data cleaned and plots generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
