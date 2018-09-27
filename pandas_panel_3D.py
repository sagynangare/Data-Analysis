import pandas as pd
import numpy as np
wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
              major_axis=pd.date_range('1/1/2000', periods=5),
              minor_axis=['A', 'B', 'C', 'D'])
print(wp)
