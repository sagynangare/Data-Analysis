import pandas as pd
import datetime
from pandas_datareader import data, wb
#import matplotlib.pyplot as plt
#from matplotlib import style

#style.use('fivethirtyeight')

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2018, 3, 12)
df = data.DataReader("XOM", "yahoo", start, end)

df['High'].plot()
#plt.legend()
#plt.show()

print(df.head())
