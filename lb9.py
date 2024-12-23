# Import required libraries 
import numpy as np 
import pandas as pd 
 
 
import seaborn as sns 
import matplotlib.pyplot as plt 
from scipy.stats import spearmanr 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error 
 
# Generate sample data (or load your dataset here) 
np.random.seed(42)  # For reproducibility 
x = np.random.rand(100) * 100  # Random values for x 
y = 2.5 * x + np.random.normal(0, 25, 100)  # Linear relation with noise 
 
# Convert data into a DataFrame 
data = pd.DataFrame({'X': x, 'Y': y}) 
 
# Compute Correlation 
pearson_corr = data.corr(method='pearson')  # Pearson Correlation 
spearman_corr, _ = spearmanr(data['X'], data['Y'])  # Spearman Rank Correlation 
 
# Linear Regression 
X = data['X'].values.reshape(-1, 1)  # Reshape for sklearn 
Y = data['Y'].values 
model = LinearRegression() 
model.fit(X, Y) 
Y_pred = model.predict(X) 
regression_coeff = model.coef_[0]  # Slope 
regression_intercept = model.intercept_  # Intercept 
mse = mean_squared_error(Y, Y_pred) 
 
# Print statistical results 

print("Pearson Correlation Coefficient Matrix:") 
print(pearson_corr) 
print("\nSpearman Rank Correlation Coefficient:", spearman_corr) 
print("\nLinear Regression Equation: Y = {:.2f}X + {:.2f}".format(regression_coeff, 
regression_intercept)) 
print("Mean Squared Error (MSE):", mse) 
 
# Plot X-Y scatter plot with regression line 
plt.figure(figsize=(8, 6)) 
plt.scatter(data['X'], data['Y'], color='blue', label='Data Points') 
plt.plot(data['X'], Y_pred, color='red', label='Regression Line') 
plt.title('X-Y Scatter Plot with Regression Line') 
plt.xlabel('X') 
plt.ylabel('Y') 
plt.legend() 
plt.show() 
 
# Plot heatmap of correlation matrix 
plt.figure(figsize=(6, 5)) 
sns.heatmap(pearson_corr, annot=True, cmap='coolwarm', fmt='.2f') 
plt.title('Heatmap of Correlation Matrix') 
plt.show() 
 
# Note: To use this script with a custom dataset, replace the sample data generation section 
#with loading your dataset using pandas (e.g., pd.read_csv).