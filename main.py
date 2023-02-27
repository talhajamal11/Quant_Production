# Importing Relevant Packages
import pandas as pd
from MarketData import MarketData
from MomentumFactors import Momentum

# Configurations of Libraries
pd.set_option('display.max_columns', 500)

if __name__ == '__main__':
    # Specify Ticker and Start/Stop Dates
    tickers = ['TSLA']
    start = '2022/01/01'
    stop = '2023/01/22'

    # Load Market Data into Pricing and Return Tables
    Tesla = MarketData(tickers, start, stop)
    prccd = Tesla.prccd()
    daily_returns = Tesla.daily_returns(prccd)
    print(prccd.head())
    print(daily_returns.head())

    # Initialize Momentum Class
    Tesla_Mom = Momentum(prccd)
    moving_avg = Tesla_Mom.moving_averages()
    print(moving_avg.head())
    momentum_factors = Tesla_Mom.momentum_factors()
    print(momentum_factors.head())

    # EMA
    ema = Tesla_Mom.ewm("Adj Close", 0.5)
    print(ema)



