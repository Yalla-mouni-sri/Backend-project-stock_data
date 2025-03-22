# import yfinance as yf # type: ignore
# import pandas as pd
# import matplotlib.pyplot as plt

# # Function to calculate performance metrics
# def calculate_performance_metrics(initial_value, final_value, returns, risk_free_rate=0.01):
#     total_returns = (final_value - initial_value) / initial_value
#     cagr = (final_value / initial_value) ** (1 / 1) - 1  # Assuming 1 year for simplicity
#     sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
#     max_drawdown = (returns.cummax() - returns).max()
    
#     return {
#         "Total Returns": total_returns,
#         "CAGR": cagr,
#         "Sharpe Ratio": sharpe_ratio,
#         "Max Drawdown": max_drawdown
#     }

# # Fetch historical data
# def fetch_historical_data(ticker, start, end):
#     stock = yf.download(ticker, start=start, end=end)
#     return stock

# # Apply Moving Average Crossover Strategy
# def apply_strategy(stock):
#     stock['Short_MA'] = stock['Close'].rolling(window=10).mean()
#     stock['Long_MA'] = stock['Close'].rolling(window=50).mean()
    
#     stock['Signal'] = 0
#     stock.loc[stock['Short_MA'] > stock['Long_MA'], 'Signal'] = 1  # Buy Signal
#     stock.loc[stock['Short_MA'] < stock['Long_MA'], 'Signal'] = -1  # Sell Signal
    
#     return stock

# # Visualize the strategy
def visualize_strategy(stock):
    plt.figure(figsize=(12,6))
    plt.plot(stock.index, stock['Close'], label='Stock Price', color='blue')
    plt.plot(stock.index, stock['Short_MA'], label='Short MA (10 days)', color='green')
    plt.plot(stock.index, stock['Long_MA'], label='Long MA (50 days)', color='red')
    
    plt.scatter(stock.index[stock['Signal'] == 1], stock['Close'][stock['Signal'] == 1], label='Buy', marker='^', color='green', alpha=1)
    plt.scatter(stock.index[stock['Signal'] == -1], stock['Close'][stock['Signal'] == -1], label='Sell', marker='v', color='red', alpha=1)
    
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.title("Moving Average Crossover Strategy")
    plt.legend()
    plt.show()


# # Main function to run the strategy
# def main():
#     ticker = "AAPL"
#     start_date = "2023-01-01"
#     end_date = "2024-01-01"
    
#     stock_data = fetch_historical_data(ticker, start_date, end_date)
#     stock_data = apply_strategy(stock_data)
    
#     # Calculate performance metrics
#     initial_value = stock_data['Close'].iloc[0]
#     final_value = stock_data['Close'].iloc[-1]
#     returns = stock_data['Close'].pct_change().dropna()
    
#     metrics = calculate_performance_metrics(initial_value, final_value, returns)
#     print(metrics)
    
#     visualize_strategy(stock_data)

# if __name__ == "__main__":
#     main()

import pandas as pd
import numpy as np

def calculate_performance_metrics(initial_value, final_value, returns):
    """Calculate total returns, CAGR, Sharpe Ratio, and Max Drawdown"""
    total_returns = (final_value - initial_value) / initial_value
    cagr = total_returns  # Assuming 1-year period for simplicity
    sharpe_ratio = returns.mean() / returns.std() if returns.std() != 0 else 0
    max_drawdown = np.max(np.maximum.accumulate(returns) - returns)

    return {
        "Total Returns": total_returns,
        "CAGR": cagr,
        "Sharpe Ratio": sharpe_ratio,
        "Max Drawdown": max_drawdown
    }

def apply_strategy(df, short_window=10, long_window=30):
    """Apply moving average crossover strategy"""
    df['Short_MA'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
    df['Long_MA'] = df['Close'].rolling(window=long_window, min_periods=1).mean()

    # Generate trading signals
    df['Signal'] = 0  # Default to no position
    df.loc[df['Short_MA'] > df['Long_MA'], 'Signal'] = 1  # Buy
    df.loc[df['Short_MA'] < df['Long_MA'], 'Signal'] = -1  # Sell

    return df

def fetch_historical_data():
    """Mock function to return some sample stock data"""
    data = {"Close": np.linspace(150, 220, 100)}  # Simulating stock prices
    return pd.DataFrame(data)
