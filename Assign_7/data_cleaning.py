import pandas as pd
from xception import DataCleaningError

def load_and_clean_data():
    try:
        df = pd.read_csv('country_wise_latest.csv')

        required_col = ['Country/Region', 'Confirmed', 'Deaths', 'Recovered', 'Active']
        for i in required_col:
            if i not in df.columns:
                raise DataCleaningError(f"Missing required column: {i}")

        df.fillna({
            'Confirmed': 0,
            'Deaths': 0,
            'Recovered': 0,
            'Active': 0
        }, inplace=True)#here we use for particular column 

        df.fillna(0, inplace=True) #and here we use for all if any columns/rows remains null

        df['Confirmed'] = df['Confirmed'].astype(int)
        df['Deaths'] = df['Deaths'].astype(int)
        df['Recovered'] = df['Recovered'].astype(int)
        df['Active'] = df['Active'].astype(int)

        return df
    
    except Exception as e:
        raise DataCleaningError(f"error is: {e}")
