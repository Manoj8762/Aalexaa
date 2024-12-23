# Import necessary libraries 
import pandas as pd 
import numpy as np 
 
# 1. Combining and Merging Datasets 
 
# Create two sample DataFrames 
sales_data_1 = pd.DataFrame({ 
    'OrderID': [1, 2, 3, 4], 
    'Product': ['Laptop', 'Tablet', 'Smartphone', 'Headphones'], 
    'Sales': [1200, 800, 1500, 300] 
}) 
 
sales_data_2 = pd.DataFrame({ 
    'OrderID': [3, 4, 5, 6], 
    'Product': ['Smartphone', 'Headphones', 'Smartwatch', 'Tablet'], 
    'Sales': [1500, 300, 200, 900] 
}) 
 
# Display the DataFrames 
print("Sales Data 1:\n", sales_data_1) 
print("\nSales Data 2:\n", sales_data_2) 
 
# Merge DataFrames based on 'OrderID' using an inner join 
merged_data = pd.merge(sales_data_1, sales_data_2, on='OrderID', how='inner', 
suffixes=('_left', '_right')) 
print("\nMerged Data (Inner Join):\n", merged_data) 
 
 
 
# Concatenate the DataFrames vertically 
combined_data = pd.concat([sales_data_1, sales_data_2], ignore_index=True) 
print("\nCombined Data (Concatenated Vertically):\n", combined_data) 
 
# 2. Reshaping Data with Melt 
 
# Create a sample DataFrame for reshaping 
reshaping_data = pd.DataFrame({ 
    'Month': ['Jan', 'Feb', 'Mar'], 
    'Product_A': [100, 150, 130], 
    'Product_B': [90, 80, 120] 
}) 
 
print("\nReshaping Data (Original):\n", reshaping_data) 
 
# Melt the DataFrame to reshape it from wide to long format 
melted_data = pd.melt(reshaping_data, id_vars=['Month'], var_name='Product', 
value_name='Sales') 
print("\nMelted Data (Long Format):\n", melted_data) 
 
# 3. Pivoting Data 
 
# Create a sample DataFrame for pivoting 
pivot_data = pd.DataFrame({ 
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar'], 
    'Product': ['Product_A', 'Product_B', 'Product_A', 'Product_B', 'Product_A', 'Product_B'], 
    'Sales': [100, 90, 150, 80, 130, 120] 
}) 
 
print("\nPivot Data (Original):\n", pivot_data) 
 
 
 
# Pivot the DataFrame to reshape it back to wide format 
pivoted_data = pivot_data.pivot(index='Month', columns='Product', values='Sales') 
print("\nPivoted Data (Wide Format):\n", pivoted_data) 
 
# 4. Handling Missing Data 
 
# Introduce some missing values 
pivoted_data.loc['Feb', 'Product_A'] = np.nan 
pivoted_data.loc['Mar', 'Product_B'] = np.nan 
print("\nPivoted Data with Missing Values:\n", pivoted_data) 
 
# Fill missing values with the mean of each column 
filled_data = pivoted_data.fillna(pivoted_data.mean()) 
print("\nFilled Data (Missing Values Handled):\n", filled_data) 
 
# 5. Summary Statistics 
print("\nSummary Statistics of Filled Data:\n", filled_data.describe())