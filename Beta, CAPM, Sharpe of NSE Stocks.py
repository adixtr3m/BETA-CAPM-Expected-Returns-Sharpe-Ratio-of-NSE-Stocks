import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import csv
import datetime

tik = ['']
def searchticker():
    stock = input("Enter Stock Name\n")
    ticker_list = csv.reader(open('C:/Users/91962/Desktop/Python For Finance/Finance Exercises/Tickers List NSE.csv', 'r'))

    for tik in ticker_list:
        if stock == tik[1]:
            print(tik)

            tickers = [tik[0], '^NSEI']
            data = pd.DataFrame()
            for t in tickers:
                data[t] = wb.DataReader(t, data_source='yahoo', start=datetime.datetime.now() - datetime.timedelta(days=5*365), end=datetime.datetime.now())['Close']
            returns = np.log(data / data.shift(1))
            coveriance = returns.cov() * 250
            cov_with_market = coveriance.iloc[0, 1]
            market_var = returns.iloc[:, 1].var() * 250
            beta = cov_with_market / market_var
            stock_expected_return = 0.0604 + beta * 0.075
            sharpe_ratio = (stock_expected_return - 0.05996) / (returns.iloc[:, 0].std() * 250 ** 0.5) # Risk Free Premium and Risk Free Returns(10 Year Gov Bond) as on 1 Oct 2020
            print("BETA = ", beta ,)
            print("CAPM Expected Return =", stock_expected_return * 100, "%")
            print("Sharpe Ratio =", sharpe_ratio * 100, "%")


searchticker()


