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
    market_data = MarketData(tickers, start, stop)
    prccd = market_data.prccd()
    daily_returns = market_data.daily_returns(prccd)

    # Initialize Momentum Class
    momentum = Momentum(prccd)
    moving_avg = momentum.moving_averages()
    momentum_factors = momentum.moving_averages()

    # EMA
    ema = momentum.ewm("Adj Close", 0.5)
    print(ema)
    print(moving_avg)



