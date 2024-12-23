import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from statsmodels.tsa.holtwinters import ExponentialSmoothing 
 
# Create sample time series data 
np.random.seed(42) 
date_range = pd.date_range(start="2022-01-01", end="2023-01-01", freq="D") 
data = pd.DataFrame({ 
    "Date": date_range, 
    "Value_A": np.random.normal(100, 10, len(date_range)), 
    "Value_B": np.random.normal(200, 20, len(date_range)), 
}) 
 
# Set Date as the index 
data.set_index("Date", inplace=True) 
 
# GroupBy Mechanics 
def groupby_mechanics(data): 
    print("\n--- GroupBy Mechanics ---") 
        # Group data by month and calculate mean 
    grouped = data.resample('M').mean() 
    print(grouped) 
    return grouped 
 
# Data Formats: Vector and Multivariate 
def data_formats(data): 
    print("\n--- Data Formats ---") 

 
    # Display data as vector 
    print("\nVector Format:") 
    print(data["Value_A"].head()) 
    
        # Display multivariate time series 
    print("\nMultivariate Time Series:") 
    print(data.head()) 
    
# Forecasting Example 
def time_series_forecasting(data): 
    print("\n--- Forecasting ---") 
        # Select a single column for forecasting 
    ts = data["Value_A"] 
    
        # Train-Test Split 
    train = ts[:int(0.8 * len(ts))] 
    test = ts[int(0.8 * len(ts)):] 
    
        # Fit the Holt-Winters Exponential Smoothing model 
    model = ExponentialSmoothing(train, seasonal="add", seasonal_periods=30).fit() 
    
        # Forecast for the test period 
    forecast = model.forecast(len(test)) 
    
        # Plot results 
    plt.figure(figsize=(12, 6)) 
    plt.plot(train, label="Train") 
    plt.plot(test, label="Test") 
    plt.plot(forecast, label="Forecast") 
    
    
    plt.legend() 
    plt.title("Time Series Forecasting") 
    plt.show() 
    
# Main function 
if __name__ == "__main__": 
    print("--- Time Series Data ---") 
    print(data.head()) 
    
        # Grouping Mechanics 
    monthly_data = groupby_mechanics(data) 
    
        # Data Formats 
    data_formats(data) 
    
    # Time Series Forecasting 
    time_series_forecasting(data)