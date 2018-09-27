import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url="http://www.delhisldc.org/Loaddata.aspx?mode=01/01/2018"
html=pd.read_html(url,header=0)
#print()
df=pd.DataFrame(html[1])
#print(len(df))
#print(df.iloc[[i for i in range(len(df))], [3]])
plt.plot(df.iloc[[i for i in range(len(df))], [2,3]])
plt.legend(['a', 'b'])
plt.show()
