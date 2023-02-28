# Importing Relevant Packages
import pandas as pd
from MarketData import MarketData
from MomentumFactors import Momentum

# Configurations of Libraries
pd.set_option('display.max_columns', 500)

if __name__ == '__main__':
    # Specify Ticker and Start/Stop Dates
    start = '2022/01/01'
    stop = '2023/01/22'

    # Load Market Data into Pricing and Return Tables
    tsla = MarketData("TSLA", start, stop)
    tsla_prccd = tsla.prccd()
    #tsla_daily_returns = tsla.daily_returns(tsla_prccd)
    print(tsla_prccd.head())
    #print(tsla_daily_returns.head())
'''
    # Initialize Momentum Class
    tsla_mom = Momentum(tsla_prccd)
    tsla_moving_avg = tsla_mom.moving_averages()
    print(tsla_moving_avg.head())
    tsla_momentum_factors = tsla_mom.momentum_factors()
    print(tsla_momentum_factors.head())

    # EMA
    ema = tsla_mom.ewm("Adj Close", 0.5)
    print(ema)

    # Load Market Data into Pricing and Return Tables
    amzn = MarketData("AMZN", start, stop)
    amzn_prccd = amzn.prccd()
    amzn_daily_returns = amzn.daily_returns(amzn_prccd)
    print(amzn_prccd.head())
    print(amzn_daily_returns.head())

    # Initialize Momentum Class
    amzn_mom = Momentum(amzn_prccd)
    amzn_moving_avg = amzn_mom.moving_averages()
    print(amzn_moving_avg.head())
    amzn_momentum_factors = amzn_mom.momentum_factors()
    print(amzn_momentum_factors.head())

    # EMA
    amzn_ema = amzn_mom.ewm("Adj Close", 0.5)
    print(amzn_ema)
'''