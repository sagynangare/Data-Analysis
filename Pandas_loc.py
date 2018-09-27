import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# series
population = pd.Series({'Germany': 81.3, 'Belgium': 11.3, 'France': 64.3, 
                        'United Kingdom': 64.9, 'Netherlands': 16.9})

#print("Series Data: \n", population)
# dataframe
data = {'country': ['Belgium', 'France', 'Germany', 'Netherlands', 'United Kingdom'],
        'population': [11.3, 64.3, 81.3, 16.9, 64.9],
        'area': [30510, 671308, 357050, 41526, 244820],
        'capital': ['Brussels', 'Paris', 'Berlin', 'Amsterdam', 'London']}
countries = pd.DataFrame(data)
print("DataFrame Data: \n",countries)


countries = countries.set_index('country')
#print(countries)

df=countries.loc['France':'Germany', ['area', 'population']]
df1=countries.iloc[0:2,1:3]
print(df)
print(df1)
"""
countries2 = countries.copy()
countries2.loc['Belgium':'Germany', 'population'] = 10
#print(countries2)
#print('Norm',countries['area'] > 100000)

#print('After',countries[countries['area'] > 100000])
#print(countries)
countries['density']=(countries['area']*1000)/countries['population']
#print(countries)
s = countries['capital']
#print(s.isin(['Berlin', 'London']))
"""
