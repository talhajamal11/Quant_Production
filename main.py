# Importing Relevant Packages
import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt
import requests


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


if __name__ == '__main__':
    end = dt.datetime.now().date()
    start = '2010/01/01'
    print(start)
    # AMZN = get_pricing('AMZN', '2020-01-01', '2022-01-01')
