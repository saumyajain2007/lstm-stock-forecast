# 📈 LSTM Stock Price Forecast

## Project Overview  
This repository demonstrates a robust solution for **time-series forecasting of stock prices** using a **Long Short-Term Memory (LSTM)** neural network, built with **TensorFlow** and **Keras**.  

The project is designed for reproducibility, leveraging **yfinance** to fetch real-time historical stock data, and includes a **Jupyter Notebook** for interactive exploration of model training, evaluation, and predictions.  

---

## 🧠 Theoretical Background  

### Why Forecast Stock Prices?  
Stock price forecasting is a classical **time-series prediction problem**. Financial markets are inherently noisy, but patterns such as trends and seasonality can be extracted using advanced models. Traditional statistical methods (like ARIMA) are often limited in capturing complex nonlinear dependencies. This is where **deep learning models** come in.  

### What is LSTM?  
**Long Short-Term Memory (LSTM)** is a type of **Recurrent Neural Network (RNN)** designed to model sequential data. Unlike standard RNNs, LSTMs can effectively capture **long-term dependencies** by using a gating mechanism that regulates the flow of information.  

- **Forget Gate**: Decides what past information to discard.  
- **Input Gate**: Selects which new information to store.  
- **Cell State**: Maintains memory across long sequences.  
- **Output Gate**: Determines the output at each time step.  

This makes LSTM particularly suitable for **financial time-series forecasting**, where past prices, trends, and volatility influence future values.  

### Why LSTM for Stock Price Forecasting?  
- **Sequential Modeling**: Captures temporal dependencies in stock data.  
- **Nonlinear Relationships**: Learns complex patterns beyond linear trends.  
- **Robustness**: Handles noisy, volatile stock market data better than many classical methods.  
- **Scalability**: Works with different assets, tickers, and time horizons.  

---

## 🚀 Key Features  
- **Data Acquisition**: Fetch historical stock price data for any ticker using the [yfinance](https://github.com/ranaroussi/yfinance) library.  
- **Data Preprocessing**: Apply scaling (`MinMaxScaler`) and generate time-series sequences for model training.  
- **Model Architecture**: Sequence-to-sequence LSTM model built with Keras for forecasting tasks.  
- **Forecasting**: Predict future stock prices and visualize forecasts against historical data.  
- **Interactive Notebook**: Step-by-step Jupyter notebook (`notebooks/LSTM_Forecasting.ipynb`) for exploration and experimentation.  
- **Code Quality**: Includes **unit tests** (`tests/`) and **GitHub Actions CI** for reliability and maintainability.  

---

## ⚙️ Installation and Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/saumyajain2007/lstm-stock-forecast.git
cd lstm-stock-forecast
```

### 2. Create and Activate Virtual Environment (Recommended)  
```bash
python -m venv venv
source venv/bin/activate   # On Linux/macOS
# .\venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

---

## 📊 Usage  

### Run the Jupyter Notebook  
```bash
jupyter notebook
```
- Open `notebooks/LSTM_Forecasting.ipynb`  
- Run all cells sequentially  
- Modify the target stock ticker, lookback window, and model parameters directly in the notebook  

### Run Unit Tests  
```bash
pytest tests/
```
This ensures data fetching, preprocessing, and model utilities are functioning correctly.  

---

## 📂 Project Structure  
```
.
├── notebooks/
│   └── LSTM_Forecasting.ipynb   # Main interactive notebook for training & analysis
├── src/
│   ├── data_loader.py           # Data fetching & preprocessing functions
│   └── model.py                 # LSTM model definition & training logic
├── tests/
│   └── test_model.py            # Unit tests for core functions
├── requirements.txt             # Project dependencies
└── README.md
```

---

## 🤝 Contributing  
Contributions are welcome!  
Please check out the upcoming **CONTRIBUTING.md** for guidelines on submitting pull requests, reporting issues, and suggesting improvements.  

---

## 📜 License  
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.  
