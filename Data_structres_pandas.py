import pandas as pd
import numpy as np
"""
Series
Syntax: s = pd.Series(data, index=index)
"""
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
#print(s.index)
d = {'b' : 1, 'a' : 0, 'c' : 2}
#print(pd.Series(d))
#print(pd.Series(d, index=['b', 'c', 'd', 'a']))
#print(s.get('f', np.nan))

"""
DataFrame
"""
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),\
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
#print(df)
#print(pd.DataFrame(d, index=['d', 'b', 'a']))

#print(pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three']))
#print(df.index)
d1 = {'one' : [1., 2., 3., 4.],'two' : [4., 3., 2., 1.]}
#print(pd.DataFrame(d1))
#print(pd.DataFrame(d, index=['a', 'b', 'c', 'd']))

"""From structured or record array"""
data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
print(pd.DataFrame(data))































