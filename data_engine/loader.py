from dotenv import load_dotenv
import os
from twelvedata import TDClient

load_dotenv()


def get_stock_data(symbol='AAPL', interval='1min', outputsize=10):
    api_key = os.getenv('TWELVE_DATA_API_KEY') or 'demo'

    td = TDClient(apikey=api_key)   #calls the Twelve Data API with the provided API key

    ts = td.time_series(    #passes the symbol, interval, and output size to the time_series method of the TDClient instance
        symbol=symbol,
        interval=interval,
        outputsize=outputsize
    ) 

    return ts.as_pandas() #returns the time series data as a pandas DataFrame


df = get_stock_data('AAPL', '1min', 10)

print(df)




# from dotenv import load_dotenv
# import pandas as pd
# # import twelvedata
# from twelvedata import TDClient
# import os
# # import requests

# load_dotenv()  # Load environment variables from .env file


# def get_stock_data(symbol='AAPL', interval='1min', outputsize=10):
#     api_key = os.getenv('TWELVE_DATA_API_KEY') or 'demo'
#     td = TDClient(apikey=api_key)
#     ts = td.time_series(
#         symbol=symbol,
#         interval=interval,
#         outputsize=outputsize
#     )
#     return ts.as_pandas()

#     # url = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&outputsize={outputsize}&apikey={api_key}'
#     # response = requests.get(url)

#     # if response.status_code == 200:
#     #     data = response.json()
#     #     if 'values' in data:
#     #         df = pd.DataFrame(data['values'])
#     #         df['datetime'] = pd.to_datetime(df['datetime'])
#     #         df.set_index('datetime', inplace=True)
#     #         return df
#     #     else:
#     #         print(f"Error fetching data for {symbol}: {data.get('message', 'Unknown.error')}")
#     # else:
#     #     print(f"HTTP error {response.status_code} for {symbol}: {response.text}")
#     #     return pd.DataFrame()


# df = get_stock_data('AAPL', '1min', 10)

# print(df)
# # print("Data fetched successfully.")