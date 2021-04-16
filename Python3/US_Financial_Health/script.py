#import codecademylib3_seaborn
import pandas as pd

gold_prices = pd.read_csv('gold_prices.csv')
print(gold_prices)
crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
print(crude_oil_prices)

import pandas_datareader.data as web
from datetime import datetime
start = datetime(1999,1,1)
end = datetime(2019,1,1)
nasdaq_data = web.DataReader('NASDAQ100', 'fred', start, end)
sap_data = web.DataReader('SP500', 'fred', start, end)
import pandas_datareader.wb as wb
gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'], start=start, end=end)
export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'], start=start, end=end)
print(export_data)




