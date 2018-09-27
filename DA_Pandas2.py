import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import quandl

api_key = open('quandlapikey.txt','r').read()

df = quandl.get("FMAC/HPI_TX", authtoken=api_key)

print(df.head())
df.plot()
plt.show()


fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#print(fiddy_states)

for abbv in fiddy_states[0][1][1:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))
