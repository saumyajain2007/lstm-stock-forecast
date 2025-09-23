import numpy as np
from sklearn.preprocessing import MinMaxScaler

def create_sequences(values, window):
    X, y = [], []
    for i in range(len(values) - window):
        X.append(values[i:i+window])
        y.append(values[i+window])
    return np.array(X), np.array(y)

def scale_series(series, scaler=None):
    if scaler is None:
        scaler = MinMaxScaler(feature_range=(0,1))
        reshaped = series.reshape(-1,1)
        scaled = scaler.fit_transform(reshaped).flatten()
        return scaled, scaler
    else:
        reshaped = series.reshape(-1,1)
        scaled = scaler.transform(reshaped).flatten()
        return scaled, scaler