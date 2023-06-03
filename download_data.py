import os

import pandas as pd
import yfinance as yf

def download_and_save(symbol):

    data = yf.download([symbol], start="1970-01-01", end="2022-12-31")

    if not os.path.exists('data/'):
        os.makedirs('data/')

    data = data.reset_index()
    data['Date'] = pd.to_datetime(data['Date']).dt.date
    data.to_csv(f'data/{symbol}.csv', index=False)

download_and_save('AAPL')
download_and_save('SPY')
