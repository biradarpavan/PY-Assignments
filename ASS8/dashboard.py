import streamlit as st
from file_handling import load_cleaned_data
from visualization import plot_total_cases, plot_top_countries, plot_daily_cases

def main():
    st.title('COVID-19 Dashboard')
    df = load_cleaned_data()

    st.sidebar.title('Filters')
 
    countries = st.sidebar.multiselect('Select countries', df['Country/Region'].unique())
    if countries:
        df = df[df['Country/Region'].isin(countries)]
 
    min = int(df['Deaths'].min())
    max = int(df['Deaths'].max())
    range = st.sidebar.slider('Select death range', min, max, (min, max))
    df = df[(df['Deaths'] >= range[0]) & (df['Deaths'] <= range[1])]

    case_type = st.sidebar.selectbox('Select case type', ['Confirmed', 'Deaths', 'Recovered'])

    st.header(f'Total {case_type} Cases by Country')
    df = df[['Country/Region', case_type]].groupby('Country/Region').sum().reset_index()
    st.bar_chart(df.set_index('Country/Region'))

    if st.sidebar.button('Show Top 10 Countries'):
        st.header('Top 10 Countries with Highest Number of Cases')
        plot_top_countries(df)
        st.image('top_countries.png')

    if st.sidebar.button('Show Daily Cases'):
        st.header('Daily New Cases')
        plot_daily_cases(df)
        st.image('daily_cases.png')
    
    if st.sidebar.button('Show Total Cases OverAll'):
        st.header('Total Cases Overall')
        plot_total_cases(df)
        st.image('total_cases.png')

main()
