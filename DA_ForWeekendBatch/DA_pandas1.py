from urllib.request import urlretrieve
import pandas as pd
import matplotlib as plt

#url="https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
#u=urlretrieve(url, 'Fremont.csv')
df=pd.read_csv('Fremont.csv')
print(df.head())
df.resample('w').sum().plot()
plt.show()
