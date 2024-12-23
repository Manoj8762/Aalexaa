# Import necessary libraries 
import numpy as np 
import pandas as pd 
 
def calculate_statistics(data, frequencies): 
    # Create a DataFrame for the frequency distribution 
    df = pd.DataFrame({'Value': data, 'Frequency': frequencies}) 
 
    # Calculate the total number of observations 
    total = df['Frequency'].sum() 
    
        # Calculate mean 
    df['Weighted_Value'] = df['Value'] * df['Frequency'] 
    mean = df['Weighted_Value'].sum() / total 
    
        # Calculate median 
    cumulative_frequency = df['Frequency'].cumsum() 
    median_index = cumulative_frequency.searchsorted(total / 2) 
    median = df['Value'][median_index] 
    
        # Calculate mode 
    mode = df['Value'][df['Frequency'].idxmax()] 
    
        # Calculate variance and standard deviation 

    variance = np.average((df['Value'] - mean) ** 2, weights=df['Frequency']) 
    std_deviation = np.sqrt(variance) 
    
        # Calculate mean deviation 
    mean_deviation = np.average(np.abs(df['Value'] - mean), weights=df['Frequency']) 
    
    # Calculate quartile deviation 
    q1 = np.percentile(data, 25) 
    q3 = np.percentile(data, 75) 
    quartile_deviation = (q3 - q1) / 2 
 
    return { 
        'Mean': mean, 
        'Median': median, 
        'Mode': mode, 
        'Variance': variance, 
        'Standard Deviation': std_deviation, 
        'Mean Deviation': mean_deviation, 
        'Quartile Deviation': quartile_deviation 
    } 
 
# Get user input for data and frequencies 
data_input = input("Enter the data values separated by commas (e.g., 10, 20, 30): ") 
frequencies_input = input("Enter the corresponding frequencies separated by commas (e.g., 1, 2, 3): ") 
 
# Convert input strings to lists of integers 
data = list(map(int, data_input.split(','))) 
frequencies = list(map(int, frequencies_input.split(','))) 
 

 
# Calculate statistics 
statistics = calculate_statistics(data, frequencies) 
 
# Display the results 
for stat, value in statistics.items(): 
    print(f"{stat}: {value:.2f}") 