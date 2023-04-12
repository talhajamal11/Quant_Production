# Importing Relevant Packages
import pandas as pd
from MarketData import MarketDataYFinance
from MomentumFactors import Momentum
from Plot import Ply
from FinanceDatabase import Equities

# Configurations of Libraries
pd.set_option('display.max_columns', 500)


def main():
    # Specify Ticker and Start/Stop Dates
    start = '2020/01/01'
    stop = '2022/12/31'

    market_data = MarketDataYFinance("TSLA", start, stop)
    price_df = market_data.price_df()
    print(price_df)

    return None


if __name__ == '__main__':
    main()
    print("Finished Executing Code")
