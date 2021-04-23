import pandas as pd
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
symbols = ["MSFT", "TSM", "ADBE", "CRM", "NOW"]
start_date = "2020-01-01"
end_date = "2020-04-22"
stock_data = web.get_data_yahoo(symbols, start_date, end_date)
print(stock_data.head())
print(stock_data['Adj Close'].head())
stock_data_closing_prices = stock_data['Adj Close']
stock_data_closing_prices.plot()
plt.xlabel("Date")
plt.ylabel("Adjusted Closing Price")
plt.title("Tech Stocks Adjusted Price Over Time")
plt.show()

stock_data_daily_returns = stock_data['Adj Close'].pct_change()
stock_data_daily_returns.plot()
plt.xlabel("Date")
plt.ylabel("ROR")
plt.title("Daily Simple Rate of Return Over time")
# plt.figure(figsize=(16,9))
plt.show()

fig = plt.figure(figsize=(13, 13))
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax1.plot(stock_data['Adj Close']['MSFT'].pct_change())
ax1.set_title("Microsoft")
ax2.plot(stock_data['Adj Close']['TSM'].pct_change())
ax2.set_title("Taiwan Semiconductor Manufacturing")
ax3.plot(stock_data['Adj Close']['ADBE'].pct_change())
ax3.set_title("Adobe")
ax4.plot(stock_data['Adj Close']['CRM'].pct_change())
ax4.set_title("Salesforce.com")
ax5.plot(stock_data['Adj Close']['NOW'].pct_change())
ax5.set_title("ServiceNow ")
plt.tight_layout()
plt.show()

# calculate daily mean
daily_mean = stock_data_daily_returns.mean()
print(daily_mean)
# daily mean index for the x axis
daily_mean.keys()
# grab each daily mean value for the y axis
height = []
for key in daily_mean.keys():
    height.append(daily_mean[key])
print(height)
# arrange keys on x axis based on length
x_pos = np.arange(len(daily_mean.keys()))
print(x_pos)
# plot bars
plt.bar(x_pos, height)

# create names on the x-axis
plt.xticks(x_pos, daily_mean.keys())

# label chart
plt.xlabel("Tech_Stocks")
plt.ylabel("daily mean")
plt.title("daily mean rate of return")

# show graphic
plt.show()

# calculate variance
daily_var = stock_data_daily_returns.var()
print(daily_var)
# variance index for the x axis
print(daily_var.keys())
# grab each variance value for the y axis
height = []
for key in daily_var.keys():
    height.append(daily_var[key])
print(height)
# arrange keys on x axis based on length
x_pos = np.arange(len(daily_var.keys()))
print(x_pos)
# plot bars
plt.bar(x_pos, height)

# create names on the x-axis
plt.xticks(x_pos, daily_var.keys())

# label chart
plt.xlabel("Tech_Stocks")
plt.ylabel("variance")
plt.title("daily variance")

# show graphic
plt.show()

# calculate standard deviation
daily_std = stock_data_daily_returns.std()
print(daily_std)
# standard deviation index for the x axis
print(daily_var.keys())
# grab each standard deviation value for the y axis
height = []
for key in daily_std.keys():
    height.append(daily_std[key])
print(height)
# arrange keys on x axis based on length
x_pos = np.arange(len(daily_std.keys()))
print(x_pos)
# plot bars
plt.bar(x_pos, height)

# create names on the x-axis
plt.xticks(x_pos, daily_std.keys())

# label chart
plt.xlabel("Tech_Stocks")
plt.ylabel("std")
plt.title("daily std")

# show graphic
plt.show()

print(stock_data_daily_returns.corr())
