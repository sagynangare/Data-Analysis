
import pandas as pd
from functools import reduce

# Display floats with 2 decimal places
pd.options.display.float_format = '{:,.2f}'.format
"""float_format = The callable should accept a floating point number and return a
string with the desired format of the number. This is used in some places like SeriesFormatte"""
 
# Expand display limits
pd.options.display.max_rows = 200
pd.options.display.max_columns = 100

# Read BNC2 sample dataset
df = pd.read_csv('BNC2_sample.csv',
                 names=['Code', 'Date', 'Open', 'High', 'Low', 
                        'Close', 'Volume', 'VWAP', 'TWAP'])
 
# Display first 5 observations
#print(df.head())
#df.loc[:, ['Code','Low','Open', 'High']]


# Unique codes in the dataset
print( df.Code.unique())

# Example of GWA and MWA relationship
print(df[df.Code.isin(['GWA_BTC', 'MWA_BTC_JPY', 'MWA_BTC_EUR']) & (df.Date == '2018-01-01')])
#Filter out MWA codes
# Number of observations in dataset
print( 'Before:', len(df) )
# Before: 31761
 
# Get all the GWA codes
gwa_codes = [code for code in df.Code.unique() if 'GWA_' in code]
 
# Only keep GWA observations
df = df[df.Code.isin(gwa_codes)]
 
# Number of observations left
print( 'After:', len(df) )
# After: 6309
#Pivot Dataset: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.pivot.html
# Pivot dataset
pivoted_df = df.pivot(index='Date', columns='Code', values='VWAP')
 
# Display examples from pivoted dataset
print(pivoted_df.tail())
#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.shift.html
print( pivoted_df.tail(3))
print(pivoted_df.tail(3).shift(1))

# Calculate returns over 7 days prior
delta_7 = pivoted_df / pivoted_df.shift(7) - 1.0
 
# Display examples
print(delta_7.tail())

# Calculate returns over each window and store them in dictionary
delta_dict = {}
for offset in [7, 14, 21, 28]:
    delta_dict['delta_{}'.format(offset)] = pivoted_df / pivoted_df.shift(offset) - 1.0

# Melt delta_7 returns
melted_7 = delta_7.reset_index().melt(id_vars=['Date'], value_name='delta_7')
 
# Melted dataframe examples
print(melted_7.tail())

# Melt all the delta dataframes and store in list
melted_dfs = []
for key, delta_df in delta_dict.items():
    melted_dfs.append( delta_df.reset_index().melt(id_vars=['Date'], value_name=key) )

# Calculate 7-day returns after the date
return_df = pivoted_df.shift(-7) / pivoted_df - 1.0
 
# Melt the return dataset and append to list
melted_dfs.append( return_df.reset_index().melt(id_vars=['Date'], value_name='return_7') )

#Reduce-merge the melted data
# Merge two dataframes
print(pd.merge(melted_dfs[0], melted_dfs[1], on=['Date', 'Code']).tail())

# Grab features from original dataset
base_df = df[['Date', 'Code', 'Volume', 'VWAP']]
 
# Create a list with all the feature dataframes
feature_dfs = [base_df] + melted_dfs

# Reduce-merge features into analytical base table
abt = reduce(lambda left,right: pd.merge(left,right,on=['Date', 'Code']), feature_dfs)
 
# Display examples from the ABT
abt.tail(10)

# Data from Sept 1st, 2017
abt[abt.Date == '2017-09-01']

#Programmatically pick highest momentum
max_momentum_id = abt[abt.Date == '2017-09-01'].delta_28.idxmax()
daily_df.loc[max_momentum_id, ['Code','return_7']]

#(Optional) Aggregate with group-by
# Create 'month' feature
abt['month'] = abt.Date.apply(lambda x: x[:7])
 
# Group by 'Code' and 'month' and keep first date
gb_df = abt.groupby(['Code', 'month']).first().reset_index()
 
# Display examples
print(gb_df.tail())

















































































