import pandas as pd

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats, index=['A', 'B','C','D','E','F'])#2-Dimentional data 
#print(df['Day'])
df=pd.Series([1,2,3,4,5],  index=['A', 'B','C','D','E'])
#print(df)
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(df)
##print(df.rename(str.lower, axis='columns'))
##print(df.rename(id, axis='index'))
##l=[[21,31,3,34,34],[4,345,34,545],[5,654,45]]
##df1=pd.DataFrame(l)
##print(df1)
