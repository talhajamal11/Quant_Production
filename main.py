# Importing Relevant Packages
import pandas as pd
from MarketData import MarketDataYFinance
from MomentumFactors import Momentum

# Configurations of Libraries
pd.set_option('display.max_columns', 500)

if __name__ == '__main__':
    # Specify Ticker and Start/Stop Dates
    start = '2022/01/01'
    stop = '2023/01/22'

    # Load Market Data into Pricing and Return Tables
    JPM = MarketDataYFinance("JPM", start, stop)
    JPM_PRCCD = JPM.prccd(price_col="Adj Close")

    JPM_MOM = Momentum(JPM_PRCCD)
    JPM_RSI_SMA = JPM_MOM.rsi(periods=14, price_col="Adj Close", ewm=False)
    JPM_RSI_EWM = JPM_MOM.rsi(periods=14, price_col="Adj Close", ewm=True)
