#import codecademylib3_seaborn
import pandas_datareader.wb as wb
from datetime import datetime
import pandas_datareader.data as web
import pandas as pd
import numpy as np
gold_prices = pd.read_csv('gold_prices.csv')
print(gold_prices)
crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
print(crude_oil_prices)

start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)
nasdaq_data = web.DataReader('NASDAQ100', 'fred', start, end)
sap_data = web.DataReader('SP500', 'fred', start, end)
gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=[
                       'US'], start=start, end=end)
export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=[
                          'US'], start=start, end=end)
print(export_data)


def log_return(prices):
    return np.log(prices / prices.shift(1))


gold_returns = log_return(gold_prices['Gold_Price'])
crudeoil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])
sap_returns = log_return(sap_data['SP500'])
gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])
export_returns = log_return(export_data['NE.EXP.GNFS.CN'])
print('gold:', gold_returns.var())
print('crudeoil:', crudeoil_returns.var())
print('nasdaq:', nasdaq_returns.var())
print('sap:', sap_returns.var())
print('gdp:', gdp_returns.var())
print('export:', export_returns.var())
