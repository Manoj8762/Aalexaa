# Import necessary libraries 
import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score 
 
# Load the Iris dataset 
data = load_iris() 
X = pd.DataFrame(data.data, columns=data.feature_names)  # Features 
y = X['petal length (cm)']  # Let's predict 'petal length' as the dependent variable 
X = X.drop(columns=['petal length (cm)'])  # Remove 'petal length' from independent variables 
 
# Split the dataset into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
 
# Apply Multiple Linear Regression 
model = LinearRegression() 
model.fit(X_train, y_train)  # Train the model 
 
# Predict on the test set 
y_pred = model.predict(X_test) 
 
# Evaluate the model 
mse = mean_squared_error(y_test, y_pred) 
r2 = r2_score(y_test, y_pred) 
 
# Print model performance metrics 
print("Multiple Linear Regression Results") 

print("----------------------------------") 
print(f"Mean Squared Error (MSE): {mse:.4f}") 
print(f"R-squared (R²): {r2:.4f}") 
print("\nModel Coefficients:") 
for feature, coef in zip(X.columns, model.coef_): 
    print(f"  {feature}: {coef:.4f}") 
    print(f"Intercept: {model.intercept_:.4f}") 
    
# Visualize actual vs predicted values 
plt.figure(figsize=(8, 6)) 
plt.scatter(y_test, y_pred, color='blue', alpha=0.7) 
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, 
linestyle='--') 
plt.title('Actual vs Predicted Values (Test Set)') 
plt.xlabel('Actual Values') 
plt.ylabel('Predicted Values') 
plt.grid() 
plt.show() 
 
 
# Pair plot to explore relationships in the dataset 
sns.pairplot(pd.DataFrame(data.data, columns=data.feature_names), diag_kind='kde') 
plt.suptitle('Pairplot of Iris Dataset Features', y=1.02) 
plt.show()