import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt


class MarketData:
    def __init__(self, tickers: list, start: str, stop: str):
        self.tickers = tickers
        self.start = dt.datetime.strptime(start, '%Y/%m/%d')
        self.stop = dt.datetime.strptime(stop, '%Y/%m/%d')

    def prccd(self):
        # This function returns a dataframe for the pricing and volume data for a single ticker
        price_df = yf.download(self.tickers, self.start, self.stop)
        price_df.dropna(inplace=True)
        return price_df

    def daily_returns(self, df):
        # Create a dataframe for the return statistics of a provided dataframe
        returns = pd.DataFrame()
        returns["Daily Returns"] = df["Adj Close"].pct_change()
        returns["Daily Log Returns"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))
        returns["Cumulative Returns"] = ((returns["Daily Returns"]) + 1).cumprod()
        returns["Annualized Volatility"] = returns["Daily Log Returns"].rolling(252).std() * np.sqrt(252)
        returns.dropna(inplace=True)
        return returns
