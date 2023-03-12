# Importing Relevant Packages
import pandas as pd
from MarketData import MarketDataYFinance
from MomentumFactors import Momentum
from Plot import Ply

# Configurations of Libraries
pd.set_option('display.max_columns', 500)


def main():
    # Specify Ticker and Start/Stop Dates
    start = '2022/01/01'
    stop = '2023/01/22'

    # Load Market Data into Pricing and Return Tables
    jpm = MarketDataYFinance("JPM", start, stop)
    jpm_prccd = jpm.prccd(price_col="Adj Close")

    jpm_mom = Momentum(jpm_prccd)
    jpm_rsi_sma = jpm_mom.rsi(periods=14, price_col="Adj Close", ewm=False)
    jpm_rsi_ewm = jpm_mom.rsi(periods=14, price_col="Adj Close", ewm=True)

    plot = Ply(jpm_prccd)
    plot = plot.line_chart(y_axis='Adj Close')

    return None


if __name__ == '__main__':
    main()
