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

    def ewm(self, column: str, n: float):
        ewm = pd.DataFrame()
        ewm["EMA"] = self.df[column].ewm(n).mean()
        ewm.dropna()
        return ewm

    def momentum_factors(self):
        mom_df = pd.DataFrame()
        mom_df["12M-1M Momentum"] = self.df["Adj Close"].shift(21) / self.df["Adj Close"].shift(252)
        mom_df["12M-2M Momentum"] = self.df["Adj Close"].shift(42) / self.df["Adj Close"].shift(252)
        mom_df.dropna(inplace=True)
        return mom_df

    def rsi(self, periods, ewm=True):

        # Calculate Difference in Daily Prices
        rsi_diff = self.df["Adj Close"].diff()

        # Create 2 different Positive and Negative Gains Series
        up = rsi_diff.clip(lower=0)
        down = rsi_diff.clip(upper=0)

        if ewm:
            # Use Exponential Moving Average
            ma_up = up.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
            ma_down = down.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
        else:
            ma_up = up.rolling(window=periods).mean()
            ma_down = down.rolling(window=periods).mean()

        rsi = ma_up/ma_down
        rsi = 100 - (100/(1 + rsi))

        return rsi
