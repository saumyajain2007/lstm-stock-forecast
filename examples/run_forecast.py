# Simple script to run a train/forecast on a symbol (AAPL example)
import numpy as np
from src.data_loader import load_price_history
from src.utils import create_sequences, scale_series
from src.model import build_lstm, train_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def main():
    symbol = 'AAPL'
    df = load_price_history(symbol, start='2018-01-01', end='2024-12-31')
    prices = df['Adj Close'].values
    scaled, scaler = scale_series(prices)
    WINDOW = 60
    X, y = create_sequences(scaled, WINDOW)
    # reshape for LSTM: (samples, timesteps, features)
    X = X.reshape((X.shape[0], X.shape[1], 1))
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = build_lstm(input_shape=(X.shape[1], X.shape[2]))
    history = train_model(model, X_train, y_train, X_val, y_val, epochs=30)
    # Forecast last window
    last_window = scaled[-WINDOW:]
    inp = last_window.reshape((1, WINDOW, 1))
    pred_scaled = model.predict(inp)[0,0]
    # invert scale
    from sklearn.preprocessing import MinMaxScaler
    dummy = MinMaxScaler(feature_range=(0,1))
    dummy.min_, dummy.scale_ = scaler.min_, scaler.scale_
    pred = dummy.inverse_transform([[pred_scaled]])[0,0]
    print(f'Next-day forecast for {symbol}:', pred)

if __name__ == '__main__':
    main()