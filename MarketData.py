import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt


class MarketData:
    def __init__(self, tic, start: str, stop: str):
        self.tic = tic
        self.start = dt.datetime.strptime(start, '%Y/%m/%d')
        self.stop = dt.datetime.strptime(stop, '%Y/%m/%d')

    def prccd(self):
        # This function returns a dataframe for the pricing and volume data for a single ticker
        price_df = yf.download(self.tic, self.start, self.stop)
        price_df["Daily Returns"] = price_df["Adj Close"].pct_change()
        price_df["Daily Log Returns"] = np.log(price_df["Adj Close"] / price_df["Adj Close"].shift(1))
        price_df["Cumulative Returns"] = ((price_df["Daily Returns"]) + 1).cumprod()
        price_df["Annualized Volatility"] = price_df["Daily Log Returns"].rolling(252).std() * np.sqrt(252)
        # price_df.dropna(inplace=True)
        return price_df
