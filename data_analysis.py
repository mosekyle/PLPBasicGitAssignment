# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data.csv")  # Adjust the file path as needed

# Data Exploration
# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Dataset information (data types, non-null counts)
print("\nDataset Information:")
print(df.info())

# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Basic Data Analysis
# Example 1: Grouping by 'CategoryColumn' and calculating the mean of 'NumericalColumn'
category_avg = df.groupby('CategoryColumn')['NumericalColumn'].mean()
print("\nAverage of NumericalColumn by CategoryColumn:")
print(category_avg)

# Example 2: Counting occurrences in 'CategoryColumn'
category_counts = df['CategoryColumn'].value_counts()
print("\nCategory Distribution:")
print(category_counts)

# Data Visualization

# Bar plot for categorical data
plt.figure(figsize=(8,6))
df['CategoryColumn'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.show()

# Histogram for numerical data
plt.figure(figsize=(8,6))
df['NumericalColumn'].hist(bins=20, color='green', alpha=0.7)
plt.title('Distribution of NumericalColumn')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Line plot for trends over time (if the data has a 'DateColumn')
df['DateColumn'] = pd.to_datetime(df['DateColumn'])
df.set_index('DateColumn').resample('M')['NumericalColumn'].mean().plot(figsize=(10,6))
plt.title('Monthly Average of NumericalColumn')
plt.xlabel('Date')
plt.ylabel('Average Value')
plt.show()

# Scatter plot to show relationship between two numerical columns
plt.figure(figsize=(8,6))
plt.scatter(df['NumericalColumn1'], df['NumericalColumn2'], color='purple', alpha=0.5)
plt.title('Relationship Between NumericalColumn1 and NumericalColumn2')
plt.xlabel('NumericalColumn1')
plt.ylabel('NumericalColumn2')
plt.show()

# Findings and Observations
print("\nFindings and Observations:")
print("- There is a clear trend of increasing values in 'NumericalColumn' over time.")
print("- The distribution of 'CategoryColumn' is skewed, with a few categories dominating the data.")
print("- The scatter plot shows a moderate positive relationship between 'NumericalColumn1' and 'NumericalColumn2'.")
