import pandas as pd
import matplotlib.pyplot as plt
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats )
print(df)
#print(df.reindex(columns=['A', 'B', 'C']))
##plt.plot(df)
##plt.show()
#print(df)
df2 = pd.DataFrame({"Name": [1, 2, 3], "Value": [4, 5, 6]})
#print(df2)
#print(df2.rename(str.lower, axis='columns'))
