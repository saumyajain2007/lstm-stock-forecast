import yfinance as yf
import pandas as pd

def load_price_history(symbol, start=None, end=None, interval='1d'):
    df = yf.download(symbol, start=start, end=end, interval=interval, progress=False)
    if df.empty:
        raise ValueError(f'No data returned for {symbol}')
    df = df[['Open','High','Low','Close','Adj Close','Volume']]
    df = df.dropna()
    return df