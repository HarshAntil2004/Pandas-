"""Empty Cells
Empty cells can potentially give you a wrong result when you analyze data."""

#Remove Rows
#One way to deal with empty cells is to remove rows that contain empty cells.
#This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
import pandas as pd
df = pd.read_csv('data.csv')
new_df = df.dropna() #Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
print(new_df.to_string()) 
print("\n")

#If you want to change the original DataFrame, use the inplace = True argument: new_df = df.dropna(inplace = True)
#Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

#Replace Empty Values
"""Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:"""

import pandas as pd
df = pd.read_csv('data.csv')
df.fillna(130,inplace= True)
print(df.to_string())
print("\n")

#Replace Only For Specified Columns
"""The example above replaces all empty cells in the whole Data Frame.

To only replace empty values for one column, specify the column name for the DataFrame:"""
import pandas as pd
df = pd.read_csv('data.csv')
df.fillna({"column":130} , inplace= True)

#Replace Using Mean, Median, or Mode
"""A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

"""
#Mean() = the average value (the sum of all values divided by number of values).
import pandas as pd
df = pd.read_csv('data.csv')
x = df["calories"].mean()
df.fillna({"calories":x},inplace=True)

#Median() = the value in the middle, after you have sorted all values ascending.
import pandas as pd
df = pd.read_csv('data.csv')
y = df["calories"].median()
df.fillna({"calories":y},inline=True)

#Mode() = the value that appears most frequently.
import pandas as pd
df = pd.read_csv('data.csv')
z = df["calories"].mode()
df.fillna({"calories":z},inplace=True)