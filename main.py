# Importing Relevant Packages
import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt
import requests

# Configurations of Libraries
pd.set_option('display.max_columns', 500)

'''
def get_pricing(ticker, start, end):
    ticker_pricing = yf.download(ticker, start=start, end=end)
    return ticker_pricing

def get_dia():
"""dataframe of info of all tickers in Dow Jones Industrial Average"""
url = 'https://www.dogsofthedow.com/dow-jones-industrial-average-companies.htm'
request = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
soup = bs(request.text, "lxml")
stats = soup.find('table',class_='tablepress tablepress-id-42 tablepress-responsive')
pulled_df =pd.read_html(str(stats))[0]
return pulled_df

def get_spy():
url = 'https://www.slickcharts.com/sp500'
request = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
soup = bs(request.text, "lxml")
stats = soup.find('table',class_='table table-hover table-borderless table-sm')
df =pd.read_html(str(stats))[0]
df['% Chg'] = df['% Chg'].str.strip('()-%')
df['% Chg'] = pd.to_numeric(df['% Chg'])
df['Chg'] = pd.to_numeric(df['Chg'])
return df

def get_qqq():
df = pd.DataFrame()
urls = ['https://www.dividendmax.com/market-index-constituents/nasdaq-100',
'https://www.dividendmax.com/market-index-constituents/nasdaq-100?page=2',
'https://www.dividendmax.com/market-index-constituents/nasdaq-100?page=3']
for url in urls:
request = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
soup = bs(request.text, "lxml")
stats = soup.find('table',class_='mdc-data-table__table')
temp =pd.read_html(str(stats))[0]
df = df.append(temp)
df.rename(columns={'Market Cap':'Market Cap $bn'},inplace=True)
df['Market Cap $bn'] = df['Market Cap $bn'].str.strip("£$bn")
df['Market Cap $bn'] = pd.to_numeric(df['Market Cap $bn'])
df = df.sort_values('Market Cap $bn',ascending=False)
return df
'''


def pricing_df(ticker, start, stop):
    # This function returns a dataframe for the pricing and volume data for a single ticker
    beg = dt.datetime.strptime(start, '%Y/%m/%d')
    end = dt.datetime.strptime(stop, '%Y/%m/%d')
    price_df = yf.download(ticker, beg, end)
    price_df.dropna(inplace=True)
    return price_df


def daily_returns(df):
    # Create a dataframe for the return statistics of a provided dataframe
    returns = pd.DataFrame()
    returns["Daily Returns"] = df["Adj Close"].pct_change()
    returns["Daily Log Returns"] = np.log(df["Adj Close"]/df["Adj Close"].shift(1))
    returns["Cumulative Returns"] = ((returns["Daily Returns"]) + 1).cumprod()
    returns["Annualized Volatility"] = returns["Daily Log Returns"].rolling(252).std() * np.sqrt(252)
    return returns


def moving_averages(df):
    # Calculate 21D and 200D Moving Averages
    m_avg = pd.DataFrame()
    m_avg["21D SMA"] = df["Adj Close"].rolling(21).mean()
    m_avg["200D SMA"] = df["Adj Close"].rolling(252).mean()
    return m_avg


if __name__ == '__main__':
    AMZN = pricing_df('AMZN', '2022/01/01', '2023/01/22')
    AMZN_returns = daily_returns(AMZN)
    AMZN_m_avg = moving_averages(AMZN)
    print(AMZN.head())
    print(AMZN_returns)
    print(AMZN_m_avg)