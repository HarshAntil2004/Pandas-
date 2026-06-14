#What is a DataFrame?
#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)
print("\n")

#Locate Row
#As you can see from the result above, the DataFrame is like a table with rows and columns.
#Pandas use the loc attribute to return one or more specified row(s)

print(df.loc[0]) #refer to the row index , Note: This example returns a Pandas Series.
print("\n")

print(df.loc[[0,1]]) #Note: When using [], the result is a Pandas DataFrame.
print("\n")

#Named Indexes
#With the index argument, you can name your own indexes.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data , index=["day1","day2","day3"])
print(df)
print("\n")

#Locate Named Indexes
#Use the named index in the loc attribute to return the specified row(s).
print(df.loc["day1"])
print("\n")

#Load Files Into a DataFrame
#If your data sets are stored in a file, Pandas can load them into a DataFrame.

import pandas as pd
df = pd.read_csv("data.csv")
print(df)