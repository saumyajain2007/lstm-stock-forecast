import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

def build_lstm(input_shape, units=50, dropout=0.2):
    model = Sequential([
        LSTM(units, input_shape=input_shape),
        Dropout(dropout),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

def train_model(model, X_train, y_train, X_val=None, y_val=None, epochs=50, batch_size=32):
    callbacks = [EarlyStopping(monitor='val_loss', patience=8, restore_best_weights=True)]
    if X_val is not None and y_val is not None:
        history = model.fit(X_train, y_train, validation_data=(X_val,y_val),
                            epochs=epochs, batch_size=batch_size, callbacks=callbacks, verbose=1)
    else:
        history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size,
                            callbacks=callbacks, verbose=1)
    return history