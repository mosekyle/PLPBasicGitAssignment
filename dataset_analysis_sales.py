import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset
    data = pd.read_csv('sales_data.csv')

    # Display the first few rows to inspect the data
    print("First few rows of the dataset:")
    print(data.head())

    # Explore the structure of the dataset
    print("\nDataset Info (Data types and missing values):")
    print(data.info())

    # Check for missing values
    print("\nMissing values in each column:")
    print(data.isnull().sum())

    # Fill or drop missing values (for this example, we fill with the mean of the column)
    data.fillna(data.mean(), inplace=True)

except FileNotFoundError:
    print("Error: The file 'sales_data.csv' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis

# Compute basic statistics of numerical columns
print("\nBasic Statistics of Numerical Columns:")
print(data.describe())

# Example of a categorical column 'Region' and numerical column 'Sales'
if 'Region' in data.columns and 'Sales' in data.columns:
    # Group by 'Region' and compute the mean of 'Sales' for each group
    region_sales_mean = data.groupby('Region')['Sales'].mean()
    print("\nAverage Sales by Region:")
    print(region_sales_mean)

# Task 3: Data Visualization

# Line chart: Trends over time (assuming 'Date' and 'Sales' columns)
if 'Date' in data.columns and 'Sales' in data.columns:
    # Convert the 'Date' column to datetime format if it's not already
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Sales'], marker='o', linestyle='-', color='b')
    plt.title('Sales Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Bar chart: Average Sales by Region
if 'Region' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.barplot(x=region_sales_mean.index, y=region_sales_mean.values, palette='viridis')
    plt.title('Average Sales by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Sales')
    plt.show()

# Histogram: Distribution of Sales
plt.figure(figsize=(10, 6))
plt.hist(data['Sales'], bins=20, color='c', edgecolor='black')
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Sales vs. Advertising (assuming 'Advertising' column exists)
if 'Advertising' in data.columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Advertising'], data['Sales'], alpha=0.6, color='g')
    plt.title('Sales vs. Advertising')
    plt.xlabel('Advertising')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.show()


# Data Loading and Exploration:
# pd.read_csv('sales_data.csv'): Loads the dataset from a CSV file.
# data.head(): Displays the first few rows of the dataset to inspect the content.
# data.info(): Gives an overview of the dataset, including data types and missing values.
# data.isnull().sum(): Checks for missing values in each column.
# Missing values are handled by filling them with the column mean using data.fillna(data.mean(), inplace=True).
# Basic Data Analysis:
# data.describe(): Displays basic statistics for numerical columns (mean, standard deviation, etc.).
# The dataset is grouped by the Region column to calculate the average sales for each region using groupby() and mean().
# Data Visualization:
# Line Chart: Plots sales trends over time. The Date column is assumed to represent dates, and Sales represents the numerical sales data.
# Bar Chart: Displays average sales by region using sns.barplot().
# Histogram: Visualizes the distribution of sales values.
# Scatter Plot: Shows the relationship between sales and advertising (assuming an 'Advertising' column exists).
