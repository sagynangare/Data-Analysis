import pandas as pd
import numpy as np
n=1000
df= pd.DataFrame({'Store': np.random.choice(['Store_1', 'Store_2'], n),
                  'Product': np.random.choice(['Product_1', 'Product_2', 'Product_3'], n),
                  'Revenue': (np.random.random(n)*50+10).round(2),
                  'Quantity': np.random.randint(1, 10, size=n)})

#print(df.head(3))
print((df.groupby(['Store', 'Product']).pipe(lambda grp: grp.Revenue.sum()/grp.Quantity.sum()).\
       unstack().round(2)))
