import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

df = pd.read_csv('EOD-V.csv')
print(type(df))
s=df['Adj_High']
df['Adj_High'].plot()
plt.legend()
plt.show()

"""
#print(df.head())
df12 = np.reshape(np.array(df['Open']),(len(df['Open']),1))
print(df12)
df1 = df['Adj_Open']
df2 = df['Adj_High']
df3 = df['Adj_Volume']
print(df1,df2,df3)
concat1= pd.concat([df1,df2,df3])
#print(concat1.head())
#print(pd.merge(df1,df2, on=['Adj_Open','Adj_High']))
#print(df.head())
'''df4 = pd.merge(df1,df3, on='Adj_Open')
df4.set_index('HPI', inplace=True)
print(df4.head())
'''
"""
