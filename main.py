# Importing Relevant Packages
import pandas as pd
from MarketData import MarketDataYFinance
from MomentumFactors import Momentum
from Plot import Plots
from FinanceDatabase import Equities

# Configurations of Libraries
pd.set_option('display.max_columns', 500)


def main():
    # Specify Ticker and Start/Stop Dates
    start = '2020/01/01'
    stop = '2020/06/30'

    tsla_price_df = MarketDataYFinance("TSLA", start, stop).price_df()
    tsla_macd = Momentum(df=tsla_price_df).macd()
    print(tsla_macd)
    figure = Plots(tsla_price_df).plot_macd(macd=tsla_macd['macd'],
                                               signal=tsla_macd['signal'],
                                               hist=tsla_macd['hist'],
                                               price='Adj Close')


    return None


if __name__ == '__main__':
    main()
    print("Finished Executing Code")
