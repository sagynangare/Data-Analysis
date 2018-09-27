import pandas as pd
import numpy as np

url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'

df = pd.read_html(url)
print(df[:5])
#print(df)
##
##match = 'Metcalf Bank'
##df_list = pd.read_html(url, match=match)
##
##dfs = pd.read_html(url, header=0, index_col=0, skiprows=range(2))
##print(dfs)
##dfs1 = pd.read_html(url, attrs={'id': 'table'})
##dfs2 = pd.read_html(url, attrs={'class': 'sortable'})
##print(np.array_equal(dfs1[0], dfs2[0]))

