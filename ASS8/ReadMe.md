# Data Visualization of COVID-19 Dataset:

In this assignment I have done the work of cleaning and analyzing the country_wise_latest.csv file of covid-19 cases.
And plot the graphs for total cases, top countries and daily cases using matplotlib and streamlit for dashboard and data visualization.

# DataSets Used:

I have downloaded and used the Covid-19(country_wise_latest.csv file) dataset from kaggle.com for Cleaning and Analysis

# Libraries used: 

The libraries I have used is pandas to save and load from the file and for data analyzing purposes.
And Matplotlib for data visualization and to plot the graphs for total cases, top countries and daily cases.
And streamlit for dashboard and data visualization.

# Instructions on How to Run the code:  

First ensure that u have downloaded the required libraries like pandas, matplotlib and streamlit.
Then Run the "analysis.py" in the terminal write this command "python analysis.py" to clean the dataset and save it to "clean_covid_data.csv" and it will generate the plots as an image form.
Then in the terminal write this command "Streamlit run dashboard.py" it will create the streamlit app into your browser.

# Document the steps taken for data visualization and dashboard creation:

Firts importing libraries like matplotlib.pyplot for plotting (plt) and streamlit for creating the web app (st).
And modules for file handling (from file_handling import load_cleaned_data) and visualization functions (from visualization import plot_total_cases, plot_top_countries, plot_daily_cases) are imported.
And used functions like labels, title, sidebar, buttons and more for data visualization.

# Include examples of code snippets demonstrating exception handling:
# E.g 
if 'New cases' not in df.columns:
    raise ValueError("The DataFrame does not contain a 'New cases' column.")

In the above E.g ,It checks if the df has a 'New cases' column before using it for plotting the chart, If the column is missing, it raises a ValueError with a message indicating that the column is missing.
