import yfinance as yf
from functools import lru_cache
import yfinance as yf
import pandas as pd


@lru_cache
def get_sp500_tickers():
    # Download S&P 500 data from Wikipedia
    sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_table = pd.read_html(sp500_url)
    sp500_df = sp500_table[0]  # First table contains the S&P 500 components

    # Get ticker symbols from the dataframe
    sp500_tickers = sp500_df['Symbol'].tolist()

    return sp500_tickers


@lru_cache
def get_best_and_worst_performing_stocks():
    # Define the list of US stocks you want to analyze
    us_stocks = get_sp500_tickers()

    # Create an empty dictionary to store percentage changes
    performance_dict = {}

    # Fetch data for each stock and calculate percentage change
    for stock_symbol in us_stocks:
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period="1d")
        if not data.empty:
            # Calculate percentage change for today
            pct_change = ((data['Close'].iloc[-1] - data['Open'].iloc[0]) / data['Open'].iloc[0]) * 100
            performance_dict[stock_symbol] = pct_change

    # Sort the dictionary by percentage change
    performance_dict = sorted(performance_dict.items(), key=lambda item: item[1], reverse=True)
    return (performance_dict[0], performance_dict[len(performance_dict) - 1])


if __name__ == "__main__":
    print(get_best_and_worst_performing_stocks())
