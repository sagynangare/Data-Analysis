import pandas as pd
import numpy as np


dta = pd.read_csv("data/health_inspection_chi.csv")
#print(dta.index)
#print(dta.columns)
#print(dta.head())

dta = dta.set_index('inspection_id')

#print(dta.head())

#Indexing
#print(dta.address)
#print(dta['address'])
#print(dta[['address', 'inspection_date']])

print("loc does label-based indexing.", dta.loc[[1965287, 1329698]])#loc does label-based indexing.
##print("'iloc' provides integer-based indexing", dta.iloc[[0, 2]])#'iloc' provides integer-based indexing


#slice notation (start:stop:step) on loc and iloc
#print(dta.iloc[:5])
#print(dta.loc[:1335320])

#print(dta.iloc[:5, [0, 5]])
#print(dta.loc[:68091, ["address", "inspection_date"]])

dta.inspection_date = dta.inspection_date.apply(pd.to_datetime)
#print(dta.inspection_date)

##def float_to_zip(zip_code):
##    if np.isnan(zip_code):
##        return np.nan
##    
##    # 0 makes sure to left-pad with zero
##    # zip codes have 5 digits
##    # .0 means, we don't want anything after the decimal
##    # f is for float
##    zip_code = "{:05.0f}".format(zip_code)
##    return zip_code

#dta.zip = dta.zip.apply(float_to_zip)
#print(dta.zip)
#print(dta.head())

#print("dtypes: ", dta.dtypes[['inspection_date', 'zip']], '\n')
#print(dta.info())


dta.resultsresults = dta.results.astype('category')
dta.risk = dta.risk.astype('category')
dta.inspection_type = dta.inspection_type.astype('category')
dta.facility_type = dta.facility_type.astype('category')

dta.select_dtypes(['category'])
#print(dta)
#del dta['location']

dta = pd.read_csv(
    "data/health_inspection_chi.csv", 
    index_col="inspection_id",
    parse_dates=["inspection_date"])

#dta = pd.read_csv("data/health_inspection_chi.csv",converters={'zip': float_to_zip},)
dta = pd.read_csv(
    "data/health_inspection_chi.csv",
    dtype={'results': 'category',
        'risk': 'category',
        'inspection_type': 'category',
        'facility_type': 'category'})

#print(dta.risk.head())

def float_to_zip(zip_code):
    # convert from the string in the file to a float
    try:
        zip_code = float(zip_code)
    except ValueError:  # some of them are empty
        return np.nan
    
    # 0 makes sure to left-pad with zero
    # zip codes have 5 digits
    # .0 means, we don't want anything after the decimal
    # f is for float
    zip_code = "{:05.0f}".format(zip_code)
    return zip_code
#print(float_to_zip('123456'))




































