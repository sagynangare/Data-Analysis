# 2. Import libraries and dataset
import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format
pd.options.display.max_rows = 200
pd.options.display.max_columns = 100
 
df = pd.read_csv('BNC2_sample.csv',
                 names=['Code', 'Date', 'Open', 'High', 'Low', 
                        'Close', 'Volume', 'VWAP', 'TWAP'])
 
# 4. Filter unwanted observations
gwa_codes = [code for code in df.Code.unique() if 'GWA_' in code]
df = df[df.Code.isin(gwa_codes)]
 
# 5. Pivot the dataset
pivoted_df = df.pivot(index='Date', columns='Code', values='VWAP')
 
# 6. Shift the pivoted dataset
delta_dict = {}
for offset in [7, 14, 21, 28]:
    delta_dict['delta_{}'.format(offset)] = pivoted_df / pivoted_df.shift(offset) - 1
    
# 7. Melt the shifted dataset
melted_dfs = []
for key, delta_df in delta_dict.items():
    melted_dfs.append( delta_df.reset_index().melt(id_vars=['Date'], value_name=key) )
 
return_df = pivoted_df.shift(-7) / pivoted_df - 1.0
melted_dfs.append( return_df.reset_index().melt(id_vars=['Date'], value_name='return_7') )
 
# 8. Reduce-merge the melted data
from functools import reduce
 
base_df = df[['Date', 'Code', 'Volume', 'VWAP']]
feature_dfs = [base_df] + melted_dfs
 
abt = reduce(lambda left,right: pd.merge(left,right,on=['Date', 'Code']), feature_dfs)
 
# 9. Aggregate with group-by.
abt['month'] = abt.Date.apply(lambda x: x[:7])
gb_df = abt.groupby(['Code', 'month']).first().reset_index()
