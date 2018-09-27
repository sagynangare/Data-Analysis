import pandas as pd
df= pd.read_csv('pincode.csv', encoding = "ISO-8859-1")
#print(df.head())
d=pd.DataFrame(df)
print(d['statename'][0])
