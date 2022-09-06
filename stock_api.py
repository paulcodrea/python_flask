import requests

import pandas as pd
from matplotlib import pyplot as plt


# Get the stock data from the API
def get_stock_data(symbol):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&outputsize=full&apikey=YOUR_API_KEY"
    r = requests.get(url)
    return r.json()


# add the data to a pandas dataframe
def add_to_dataframe(data):
    df = pd.DataFrame(
        columns=['date', 'open', 'high', 'low', 'close', 'volume'])
    for date in data['Time Series (Daily)'].keys():
        data_row = [
            date, data['Time Series (Daily)'][date]['1. open'],
            data['Time Series (Daily)'][date]['2. high'],
            data['Time Series (Daily)'][date]['3. low'],
            data['Time Series (Daily)'][date]['4. close'],
            data['Time Series (Daily)'][date]['5. volume']
        ]
        df.loc[-1, :] = data_row
        df.index = df.index + 1
    return df


# only select data between a data range
def select_data(df, start_date, end_date):
    return df[(df['date'] >= start_date) & (df['date'] <= end_date)]


# plot the data
def plot_data(df):
    plt.plot(df['date'], df['close'])
    plt.show()


def stock_api(symbol, start_date, end_date):
    data = get_stock_data(symbol)

    df = add_to_dataframe(data)
    df = select_data(df, start_date, end_date)

    return df

def save_to_csv(df, symbol):
    # save in static folder
    df.to_csv('static/' + symbol + '.csv', index=False)

# main function
def main():
  symbol = "GOOGL"
  data = get_stock_data(symbol)
  
  df = add_to_dataframe(data)
  df = select_data(df, '2020-01-01', '2022-09-06')
  
  save_to_csv(df, symbol)


main()
