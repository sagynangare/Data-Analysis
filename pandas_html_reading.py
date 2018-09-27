#s="http://www.delhisldc.org/Loaddata.aspx?mode=25/07/2018"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# read the data from the downloaded CSV file.
data = pd.read_csv('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')
# set a numeric id for use as an index for examples.
data['id'] = [random.randint(0,1000) for x in range(data.shape[0])]
 
#print(data.head())
"""
# Single selections using iloc and DataFrame
# Rows:
print("first row of data frame: ",data.iloc[0]) # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
print("second row of data frame",data.iloc[1]) # second row of data frame (Evan Zigomalas)
print(data.iloc[-1]) # last row of data frame (Mi Richan)
# Columns:
print(data.iloc[:,0])# first column of data frame (first_name)
print(data.iloc[:,1]) # second column of data frame (last_name)
print(data.iloc[:,-1]) # last column of data frame (id)



# Multiple row and column selections using iloc and DataFrame
print(data.iloc[0:5]) # first five rows of dataframe
print(data.iloc[:, 0:2]) # first two columns of data frame with all rows
print(data.iloc[[0,3,6,24], [0,5,6]]) # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
print(data.iloc[0:5, 5:8]) # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).
"""




















