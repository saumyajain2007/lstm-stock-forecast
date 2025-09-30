# 📈 LSTM Stock Price Forecast

## Project Overview  
This repository demonstrates a robust solution for **time-series forecasting of stock prices** using a **Long Short-Term Memory (LSTM)** neural network, built with **TensorFlow** and **Keras**.  

The project is designed for reproducibility, leveraging **yfinance** to fetch real-time historical stock data, and includes a **Jupyter Notebook** for interactive exploration of model training, evaluation, and predictions.  

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
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
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
pytest
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
