import pandas as pd

#ratings of top movies
mov = pd.read_csv('http://bit.ly/imdbratings')

#print head. It will print first 5 rows
#print (mov.head())

#printing the shape. It will print rows and cloumns
print ("shape is like ",mov.shape)

#filter out the row duration.
#print (mov['duration'].head())

#Creating booleans (True/False) list of duration.
booleans = []
for i in mov.duration:
	if i >= 200:
		booleans.append(True)
	else:
		booleans.append(False)

#Printing first 5 elemnets of booleans list.
#print (booleans[:5])

#Printing length of the list and it should be equals to number of rows.
#print (len(booleans))

#Creating the series using booleans list.
is_long = pd.Series(booleans)

#printing the head of series.
#print (is_long.head())

#printing whole row using panadas series.
##print (mov[is_long].head())
##		 
##is_long = mov.duration >=200
##print (mov[is_long].head())
##
##print(mov[mov.duration >=200].actors_list)
##print(mov[mov.duration >=200]['actors_list'])
##print(mov.loc[mov.duration >=200,'actors_list'])
