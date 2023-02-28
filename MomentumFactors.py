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


    def RSI(self, n):
        RSI = pd.DataFrame()
        # Calculate Rolling Gains
        RSI["positive gains"] = self.df["Adj Close"].rolling(n).query()
        if self.df["Adj Close"] > self.df["Adj Close"].shift(1):
            rolling_gains = 10
        else :
            rolling_losses = 10
        return RSI