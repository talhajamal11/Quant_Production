# Importing Relevant Packages
import pandas as pd
from MarketData import MarketData
from MomentumFactors import Momentum

# Configurations of Libraries
pd.set_option('display.max_columns', 500)

if __name__ == '__main__':
    tickers = ['AMZN']
    market_data = MarketData(tickers)
    pricing = market_data.prccd('2022/01/01', '2023/01/22')
    print(pricing.head())

    returns = market_data.daily_returns(pricing)
    print(returns.head())

    Momentum = Momentum(pricing)
    print(Momentum.moving_averages().head())
    print(Momentum.momentum_factors().head())



