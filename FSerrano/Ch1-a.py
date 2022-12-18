# Chapter 1 
import pandas as pd

# <<<<<<< HEAD
df = pd.read_csv('classfiles/gapminder/gapminder.tsv', sep='\t')

print(type(df))
# =======
# Chapter 1.2
df = pd.read_csv('classfiles/gapminder/gapminder.tsv', sep='\t')

# Getting the head of the file
# print(df.head())

# Getting the DataFrame type 
# print(type(df))

# use shape to get the number of rows and columns.
# print(df.shape)

# Getting the columns in the file
# print(df.columns)

# Get the dtype of each column
# print(df.dtypes)

# Get more information about our data
# print(df.info())


# Chapter 1.3
# Get the country columna and name it as it's own varialbe
country_df = df['country']

# show the first 5 observations
# print(country_df.head())

# show the last 5 observations
# print(country_df.tail())

# Looking at country, continent, and year
# subset = df[['country', 'continent', 'year']]
# print(subset.head())
# print('###')
# print(subset.tail())

# Get the frist row
# print(df.loc[0])

# Get the 100th row
# print(df.loc[99])

# Get the last row /with error
# print(df.loc[-1])

# Get the last row (correctly)
# number_of_rows = df.shape[0]
# Subtract 1 from the value since we want the last index
# last_row_index = number_of_rows - 1
# now do the subset using the index of the last row
# print(df.loc[last_row_index])
# print('###')
# There are many ways to get what you want (last row)
# print(df.tail(n=1))

# subset_loc = df.loc[0]
# subset_head = df.head(n=1)
# Type of using loc of 1 row
# print(type(subset_loc))
# print("####")
# Type of using head of 1 row
# print(type(subset_head))

# Select the first, 100th, and 1000th row
# print(df.loc[[0, 99, 999]])

# Get the 2nd row
# print(df.iloc[1])
# Get the 100th row
# print(df.iloc[99])
# Using -1 to get the last row
# print(df.iloc[-1])

# Get the first, 100th, and 1000th rows
print(df.iloc[[0, 99, 999]])
# >>>>>>> dd4f1db1d4c726342e5e2e0f4c8703a1376199b1