import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import codecademylib3_seaborn
import glob


files = glob.glob("states*.csv")
us_census = []
for filename in files:
  data = pd.read_csv(filename)
  us_census.append(data)

df = pd.concat(us_census)

print(df.dtypes)
print(df.head())
print(len(df))

# for i in range(10):
#     f = open("states" + str(i) + ".csv", "w")
#     f.write("")
#     f.close()

df['Income'] = pd.to_numeric(df.Income.replace('[\$]', '', regex=True))
print(df.dtypes)
print(df.head())
df_tmp = df['GenderPop'].str.split('_')
df['Men'] = pd.to_numeric(df_tmp.str.get(0).replace('[M]', '', regex=True))
df['Women'] = pd.to_numeric(df_tmp.str.get(1).replace('[F]', '', regex=True))
print(df.dtypes)
print(df.head())
plt.scatter(df['Women'], df['Income']) 
plt.show()
#print(df.Women)
df.Women = df.Women.fillna(value=(df.TotalPop - df.Men))
#print(df.Women)
duplicates = df.duplicated()
print(duplicates.value_counts())
df_tmp = df.drop_duplicates()
df = df_tmp
plt.scatter(df['Women'], df['Income']) 
plt.show()
print(df.columns)
df['Hispanic'] = pd.to_numeric(df.Hispanic.replace('[%]', '', regex=True))
df['White'] = pd.to_numeric(df.White.replace('[%]', '', regex=True))
df['Black'] = pd.to_numeric(df.Black.replace('[%]', '', regex=True))
df['Native'] = pd.to_numeric(df.Native.replace('[%]', '', regex=True))
df['Asian'] = pd.to_numeric(df.Asian.replace('[%]', '', regex=True))
df['Pacific'] = pd.to_numeric(df.Pacific.replace('[%]', '', regex=True))
print(df.head())
nans = df.isnull()
print(nans)
Pnan = df.Pacific.isnull()
print(Pnan.value_counts())
nan_value = df.Pacific.mean()
df.Pacific = df.Pacific.fillna(value=nan_value)
Pnan = df.Pacific.isnull()
print(Pnan.value_counts())



