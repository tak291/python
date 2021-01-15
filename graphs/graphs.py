import pandas as pd 

df = pd.read_csv('/home/kike/Programming/python/graphs/graphs/assignment.csv',header=None, skiprows=1)


#Printing the first 10 columns
#print (df.head(1))


location = df[0]
dates = df[1]
orders = df[2]
percentage = df[3]

print(location)