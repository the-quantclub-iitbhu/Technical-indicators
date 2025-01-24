# Technical Indicators

A Python library for computing commonly used technical indicators in financial markets. This repository provides efficient and easy-to-use implementations of indicators that are vital for analyzing market trends, generating signals, and backtesting strategies.

---

## 📊 Supported Indicators

Currently, the library includes the following technical indicators:  
- **Supertrend**: Identifies trends and generates buy/sell signals based on volatility.  
- **RSI (Relative Strength Index)**: Measures the magnitude of recent price changes to evaluate overbought or oversold conditions.  
- **Stochastic Oscillator**: Compares a specific closing price to a range of its prices over time.  
- **ADX (Average Directional Index)**: Quantifies trend strength and direction.  
- **Bollinger Bands**: Identifies overbought or oversold market conditions using a simple moving average and standard deviation.  
- **Heikin Ashi**: Smooths out price action for clearer trend identification.  

> 🚀 **Planned Additions**:  
> This library is a work in progress. We aim to continuously expand it by adding more indicators, including:  
> - Moving Average Convergence Divergence (**MACD**)  
> - Fibonacci Retracement Levels  
> - Ichimoku Cloud  
> - Pivot Points  
> - Average True Range (**ATR**)  

---

## 🛠️ How to Use

1. **Clone the Repository**  
   Start by cloning this repository to your local system:
   ```bash
   git clone https://github.com/your-username/technical-indicators.git
   cd technical-indicators
   ```

2. **Install Dependencies**  
   Install the required Python libraries using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run an Indicator Script**  
   Execute one of the indicator scripts to calculate values. For example:
   ```bash
   python indicators/rsi.py
   ```

4. **Integrate with Your Project**  
   Import the indicator functions into your own trading strategy or application.  
   Example:
   ```python
   from indicators.supertrend import calculate_supertrend

   # Example usage:
   supertrend_df = calculate_supertrend(data, period=10, multiplier=3)
   ```

## 🎯 Objectives

This repository aims to:  
- Provide **accurate implementations** of commonly used technical indicators.  
- Grow into a **comprehensive library** for building and testing trading systems.  
- Help traders and developers **learn, experiment, and innovate** in financial markets.  

---

## 🤝 Contributions

We welcome contributions to help grow this library!  
If you would like to contribute:
1. Fork the repository.
2. Add your implementation in the `indicators/` directory.
3. Create a pull request explaining the added indicator and its use.

Feel free to suggest new indicators or enhancements by [opening an issue](https://github.com/your-username/technical-indicators/issues).

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 💬 Feedback and Support

For questions, feedback, or suggestions, please open an issue in the repository or reach out to the maintainer.

Stay tuned for updates as we continue to enhance and expand this library of technical indicators. 🚀
