# Importing Relevant Packages
import pandas as pd
from MarketData import MarketData
from MomentumFactors import Momentum

# Configurations of Libraries
pd.set_option('display.max_columns', 500)

if __name__ == '__main__':
    tickers = ['AMZN']
    market_data = MarketData(tickers, '2022/01/01', '2023/01/22')
    print(market_data.prccd().head())
    print(market_data.daily_returns(market_data.prccd()).head())

    Momentum = Momentum(market_data.prccd())
    print(Momentum.moving_averages().head())
    print(Momentum.momentum_factors().head())



