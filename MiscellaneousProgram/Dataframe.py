import pandas as pd
import matplotlib.pyplot as plt

# Create a 2D table
data = {
    'A': [1, 2, 3, 4, 5, 6],
    'B': [7, 8, 9, 10, 11, 12],
    'C': [13, 14, 15, 16, 17, 18]
}

df = pd.DataFrame(data)

# Display the first 6 rows
print("First 6 rows:")
print(df.head(6))

# Display the last 2 rows
print("Last 2 rows of the DataFrame:")
print(df.tail(2))

# Display the 4th row
print("4th row of the DataFrame:")
print(df.iloc[3])

# Display information about the DataFrame
print("Information about the DataFrame:")
df.info()

# Check for null values in the DataFrame
print("Null values in the DataFrame:",df.isnull().sum())  # Sum of null values in each column

# Check for duplicated records in the DataFrame
print("Duplicated rows in the DataFrame:", df.duplicated().sum())  # Number of duplicated rows

# Find the correlation between the columns in the DataFrame
print("Correlation between columns:")
print(df.corr())

# Change the index of the DataFrame to specific label values
df.index = ['a', 'b', 'c', 'd', 'e', 'f']
print("DataFrame with new index:")
print(df)

# 1D tableand display information about it
series = pd.Series([10, 20, 30, 40, 50])
print("Information about the 1D table (Series):")
series.info()

# Show the datatype of each column
print("Data types of each column in the DataFrame:")
print(df.dtypes)

# Plot the DataFrame 
df.plot(kind='line', x='A', y='B', title='A vs B', marker='o')  # Example plot
plt.show()
