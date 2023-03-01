import pandas as pd


class Momentum:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def moving_averages(self):
        # Calculate 21D and 200D Moving Averages
        m_avg = pd.DataFrame()
        m_avg["Adj Close"] = self.df["Adj Close"]
        m_avg["21D SMA"] = self.df["Adj Close"].rolling(21).mean()
        m_avg["200D SMA"] = self.df["Adj Close"].rolling(252).mean()
        m_avg.dropna(inplace=True)
        return m_avg

    def momentum_factors(self):
        mom_df = pd.DataFrame()
        mom_df["12M-1M Momentum"] = self.df["Adj Close"].shift(21) / self.df["Adj Close"].shift(252)
        mom_df["12M-2M Momentum"] = self.df["Adj Close"].shift(42) / self.df["Adj Close"].shift(252)
        mom_df.dropna(inplace=True)
        return mom_df

    def rsi(self, periods, ewm=True):

        rsi = pd.DataFrame()

        # Adding Daily Returns to RSI Dataframe
        rsi["Adj Close"] = self.df["Adj Close"]

        # Calculate Difference in Daily Prices
        rsi["diff"] = rsi["Adj Close"].diff()

        # Create 2 different Positive and Negative Gains Series - negative gains have to be absolute
        rsi["up"] = rsi["diff"].clip(lower=0)
        rsi["down"] = rsi["diff"].clip(upper=0).abs()

        # Check if we want RSI to use ewm or sma
        if ewm:
            # Use Exponential Moving Average
            rsi["ma_up"] = rsi["up"].ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
            rsi["ma_down"] = rsi["down"].ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
        else:
            rsi["ma_up"]= rsi["up"].rolling(window=periods).mean()
            rsi["ma_down"] = rsi["down"].rolling(window=periods).mean()

        rsi["1st Step"] = rsi["ma_up"]/rsi["ma_down"]
        rsi["RSI"] = 100 - (100/(1 + rsi["1st Step"]))

        return rsi
