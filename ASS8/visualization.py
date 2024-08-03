import matplotlib.pyplot as plt

def plot_total_cases(df):
    plt.figure(figsize=(8, 8))
    totals = df[['Confirmed', 'Deaths', 'Recovered']].sum()
    totals.plot(kind='bar')
    plt.title('Total Confirmed, Deaths, and Recovered Cases')
    plt.xlabel('Case Type')
    plt.ylabel('Number of Cases')
    plt.savefig('total_cases.png')

def plot_top_countries(df):
    df_top = df.groupby('Country/Region')['Confirmed'].sum().nlargest(10).reset_index()
    plt.figure(figsize=(10, 5))
    plt.bar(df_top['Country/Region'], df_top['Confirmed'], color='red')
    plt.xlabel('Country/Region')
    plt.ylabel('Number of Confirmed Cases')
    plt.title('Top 10 Countries with the Highest Number of Confirmed Cases')
    plt.savefig('top_countries.png')

def plot_daily_cases(df):
    if 'New cases' not in df.columns:
        raise ValueError("The DataFrame does not contain a 'New cases' column.")
    plt.figure(figsize=(15, 10))
    plt.pie(df['New cases'], labels=df['Country/Region'], autopct='%1.1f%%')
    plt.title('Daily New cases')
    plt.savefig('daily_cases.png')
    return 
