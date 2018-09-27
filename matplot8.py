import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('fivethirtyeight')
df=pd.read_csv('first_csv.csv')
st=sorted(df['Value'])
#print(st)
plt.plot(st)
plt.show()
