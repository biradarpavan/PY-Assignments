# COVID-19 Data Cleaning and Analysis:
In this assignment I have done the work of cleaning and analyzing the country_wise_latest.csv file of covid-19 cases.

# DataSets Used:
I have downloaded and used the Covid-19(country_wise_latest.csv file) dataset from kaggle.com for Cleaning and Analysis

# Libraries used: 
The libraries I have used is pandas to save and load from the file and for data analyzing purposes.

# Instructions on How to Run the code:  
First ensure that u have downloaded the required libraries like pandas ,etc.
Then Run the "data_cleaning.py"  to clean the dataset and save it to "clean_covid_data.csv".
Then Run the "analysis.py" to perform basic analysis on the cleaned dataset.

# The steps taken for data cleaning, file handling, and exception handling.

**For Data cleaning**:
Load the dataset using pandas as pd.
Handle missing values by filling them with 0 values.
Ensuring that the data types of the column is proper.
Saved the cleaned dataset into "clean_covid_data.csv".

**For File Handling**:
Saved the cleaned dataset using "save_cleaned_data" function.
Load the cleaned dataset using "load_cleaned_data" function.

**Exception Handling**: 
Define custom exceptions in "xceptions.py".
Raise exceptions for missing columns using 'DataCleaningError' and for file errors created 'FileHandlingError'

# Example :
try:
    cleaned_data = load_and_clean_data()
    save_cleaned_data(cleaned_data)
except DataCleaningError as e:
    print(f(Error occured: {e}))