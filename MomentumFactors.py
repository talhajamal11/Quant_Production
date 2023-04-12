import pandas as pd


class Momentum:
    """
    This Class has functions that return DataFrames with moving averages and momentum factors
    Initialize this class with a DataFrame of Pricing Data
    """
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def moving_averages(self, price_col: str = 'Adj Close') -> pd.DataFrame:
        """
        The only input needed for this function is the pricing column of the DataFrame
        """

        # Calculate 21D and 200D Moving Averages
        df = pd.DataFrame()
        df[price_col] = self.df[price_col]
        df["21D SMA"] = self.df[price_col].rolling(21).mean()
        df["200D SMA"] = self.df[price_col].rolling(252).mean()
        df.dropna(inplace=True)

        return df

    def momentum_factors(self, price_col: str = 'Adj Close') -> pd.DataFrame:
        """
        The only input needed for this function is the pricing column of the DataFrame
        """
        df = pd.DataFrame()
        df["12M-1M Momentum"] = self.df[price_col].shift(21) / self.df[price_col].shift(252)
        df["12M-2M Momentum"] = self.df[price_col].shift(42) / self.df[price_col].shift(252)
        df.dropna(inplace=True)

        return df

    def rsi(self, periods: int, price_col: str = 'Adj Close', ewm: bool = True) -> pd.DataFrame:
        """
        The only input needed for this function is the pricing column, periods back to calculate RSI for,
        and whether Exponential Weighted Mean is supposed to be used or a Simple Moving Average - True indicates
        EWM and False indicates SMA
        """
        df = pd.DataFrame()

        # Adding Daily Returns to RSI Dataframe
        df[price_col] = self.df[price_col]

        # Calculate Difference in Daily Prices
        df["diff"] = df[price_col].diff()

        # Create 2 different Positive and Negative Gains Series - negative gains have to be absolute
        df["up"] = df["diff"].clip(lower=0)
        df["down"] = df["diff"].clip(upper=0).abs()

        # Check if we want RSI to use ewm or sma
        if ewm:
            # Use Exponential Moving Average
            df["ma_up"] = df["up"].ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
            df["ma_down"] = df["down"].ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
        else:
            df["ma_up"] = df["up"].rolling(window=periods).mean()
            df["ma_down"] = df["down"].rolling(window=periods).mean()

        df["1st Step"] = df["ma_up"]/df["ma_down"]
        df["RSI"] = 100 - (100/(1 + df["1st Step"]))

        return df

    def macd(self, slow: int = 26, fast: int = 12, smooth: int = 9, price_col: str = 'Adj Close') -> pd.DataFrame:
        """
        Generates a DF with data for MACD
        :param slow: Default is 26
        :param fast: Default is 12
        :param smooth: Default is 9
        :param price_col: Default is Adj Close
        :return: Returns a DF for MACD data
        """
        df = pd.DataFrame()
        df["fast ewm"] = self.df[price_col].ewm(span=fast, adjust=False).mean()
        df["slow ewm"] = self.df[price_col].ewm(span=slow, adjust=False).mean()
        df["macd"] = df["fast ewm"] - df["slow ewm"]
        df["signal"] = df["macd"].ewm(span=smooth, adjust=False).mean()
        df["hist"] = df["macd"] - df["signal"]
        return df
