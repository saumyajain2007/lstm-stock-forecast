import numpy as np
from src.utils import create_sequences, scale_series

def test_create_sequences():
    arr = np.arange(10)
    X,y = create_sequences(arr, window=3)
    assert X.shape[0] == 7
    assert X.shape[1] == 3
    assert y.shape[0] == 7

def test_scale_series_roundtrip():
    arr = np.array([1.0,2.0,3.0,4.0])
    scaled, scaler = scale_series(arr)
    assert scaled.min() >= 0.0 and scaled.max() <= 1.0