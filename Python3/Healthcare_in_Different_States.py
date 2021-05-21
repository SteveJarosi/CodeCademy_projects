#import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
print(healthcare.head())
print(healthcare["DRG Definition"].unique())
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]
print(alabama_chest_pain)
costs = alabama_chest_pain[' Average Covered Charges '].values
plt.boxplot(costs)
plt.show()
states = healthcare["Provider State"].unique()
print(states)
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)
plt.figure(figsize=(20,6))
plt.boxplot(datasets, labels=states)
plt.show()
datasets2 = []
for state in states:
  datasets2.append(chest_pain[chest_pain['Provider State'] == state]['Average Medicare Payments'].values)
plt.figure(figsize=(20,6))
plt.boxplot(datasets2, labels=states)
plt.show()