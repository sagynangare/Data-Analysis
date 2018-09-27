import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('pincode.csv', skipinitialspace=True, encoding = "ISO-8859-1")
print(df.head())
c=list(df['pincode'])
plt.plot(c)
plt.show()
