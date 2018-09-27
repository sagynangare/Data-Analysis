import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()#Returns cumulative sum of series axis
#ts.plot()
#plt.show()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()

#df.plot()
#plt.show()

df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df3['A'] = pd.Series(list(range(len(df))))
#df3.plot(x='A', y='B')
#plt.show()

#df.iloc[5].plot(kind='bar');
#plt.show()

df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
#df2.plot.bar();
#plt.show()

#df2.plot.bar(stacked=True)
#plt.show()














