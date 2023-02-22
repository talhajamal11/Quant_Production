# Importing Relevant Packages
import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt

# Configurations of Libraries
pd.set_option('display.max_columns', 500)


def pricing_df(ticker, start, stop):
    # This function returns a dataframe for the pricing and volume data for a single ticker
    beg = dt.datetime.strptime(start, '%Y/%m/%d')
    end = dt.datetime.strptime(stop, '%Y/%m/%d')
    price_df = yf.download(ticker, beg, end)
    price_df.dropna(inplace=True)
    return price_df


def daily_returns(df):
    # Create a dataframe for the return statistics of a provided dataframe
    returns = pd.DataFrame()
    returns["Daily Returns"] = df["Adj Close"].pct_change()
    returns["Daily Log Returns"] = np.log(df["Adj Close"]/df["Adj Close"].shift(1))
    returns["Cumulative Returns"] = ((returns["Daily Returns"]) + 1).cumprod()
    returns["Annualized Volatility"] = returns["Daily Log Returns"].rolling(252).std() * np.sqrt(252)
    return returns


def moving_averages(df):
    # Calculate 21D and 200D Moving Averages
    m_avg = pd.DataFrame()
    m_avg["Adj Close"] = df["Adj Close"]
    m_avg["21D SMA"] = df["Adj Close"].rolling(21).mean()
    m_avg["200D SMA"] = df["Adj Close"].rolling(252).mean()
    return m_avg


def momentum_factors(df):
    mom_df = pd.DataFrame()
    mom_df["12M-1M Momentum"] = df["Adj Close"].shift(21) / df["Adj Close"].shift(252)
    mom_df["12M-2M Momentum"] = df["Adj Close"].shift(42) / df["Adj Close"].shift(252)
    return mom_df


if __name__ == '__main__':
    AMZN = pricing_df('AMZN', '2022/01/01', '2023/01/22')
    AMZN_returns = daily_returns(AMZN)
    AMZN_m_avg = moving_averages(AMZN)
    AMZN_12M_1M = momentum_factors(AMZN)
