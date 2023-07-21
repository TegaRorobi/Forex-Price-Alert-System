import requests
from decouple import config

API_KEY = config('ALPHAVANTAGE_API_KEY')

params = {
    'function' : 'TIME_SERIES_INTRADAY',
    'interval' : '5min',
    'symbol'   : 'IBM',
}

endpoint = f"https://www.alphavantage.co/query?function={params['function']}&symbol={params['symbol']}&interval={params['interval']}&apikey={API_KEY}"
response = requests.get(endpoint)
print(response.json())