import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('countries.csv')
#print(data.head())

#compare the population growth in the US and India
#print(data[data.country=='United States'])

us= data[data.country=='United States']
ind= data[data.country=='India']
plt.plot(us.year, us.population/10**6)
plt.plot(ind.year, ind.population/10**6)
plt.legend(["India", 'US'])
plt.xlabel('India')
plt.ylabel('US')
#plt.show()
print(ind.loc[:,["year"]])
#print(ind.population.iloc[0])
