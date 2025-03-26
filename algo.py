import pandas as pd
import numpy as np

# Simple Moving Average Crossover Trading Strategy
def simple_trading_strategy(prices, short_window=20, long_window=50):
    # Create a DataFrame to store our data
    df = pd.DataFrame(prices, columns=['price'])
    
    # Calculate moving averages
    df['short_ma'] = df['price'].rolling(window=short_window).mean()
    df['long_ma'] = df['price'].rolling(window=long_window).mean()
    
    # Initialize signals column
    df['signal'] = 0
    
    # Generate trading signals
    # 1 = Buy, -1 = Sell, 0 = Hold
    df['signal'][short_window:] = np.where(
        df['short_ma'][short_window:] > df['long_ma'][short_window:], 
        1, 0
    )
    
    # Create positions column (shifts signal by 1 day)
    df['position'] = df['signal'].diff()
    
    return df

# Example usage with dummy data
if __name__ == "__main__":
    # Generate sample price virtues
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', periods=200, freq='D')
    prices = np.random.normal(100, 10, 200).cumsum()
    
    # Run the strategy
    results = simple_trading_strategy(prices)
    
    # Print results
    print("Trading Signals and Positions:")
    print(results.tail())
    
    # Basic performance metrics
    total_trades = len(results[results['position'] != 0])
    print(f"\nTotal number of trades: {total_trades}")
    
    # Simple visualization
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(12, 6))
    plt.plot(results['price'], label='Price')
    plt.plot(results['short_ma'], label=f'{short_window}-day MA')
    plt.plot(results['long_ma'], label=f'{long_window}-day MA')
    
    # Plot buy signals
    plt.plot(results[results['position'] == 1].index,
             results['short_ma'][results['position'] == 1],
             '^', markersize=10, color='g', label='Buy Signal')
    
    # Plot sell signals
    plt.plot(results[results['position'] == -1].index,
             results['short_ma'][results['position'] == -1],
             'v', markersize=10, color='r', label='Sell Signal')
    
    plt.title('Simple Moving Average Crossover Strategy')
    plt.legend()
    plt.show()
