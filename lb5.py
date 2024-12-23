# Import necessary libraries 
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut 
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score 
from sklearn.linear_model import LinearRegression 

 
from sklearn.datasets import fetch_california_housing 
 
# Load the California housing dataset 
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names) 
y = pd.Series(data.target) 

# Function to calculate and display metrics 
def display_metrics(y_true, y_pred): 
    rmse = np.sqrt(mean_squared_error(y_true, y_pred)) 
    mae = mean_absolute_error(y_true, y_pred) 
    r2 = r2_score(y_true, y_pred) 
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}") 
    print(f"Mean Absolute Error (MAE): {mae:.4f}") 
    print(f"R² Score: {r2:.4f}") 
    return rmse, mae, r2 
    
# Validation Set Approach 
def validation_set_approach(X, y): 
    print("Validation Set Approach:") 
        # Split the dataset into training (80%) and validation (20%) sets 
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42) 
    
        # Initialize and train the model 
    model = LinearRegression() 
    model.fit(X_train, y_train) 
    
        # Make predictions on the validation set 
    y_pred = model.predict(X_val) 

    
    
        # Display metrics 
    display_metrics(y_val, y_pred) 
 
# Leave-One-Out Cross-Validation (LOOCV) Approach 
def loocv_approach(X, y): 
    print("Leave-One-Out Cross-Validation (LOOCV):") 
    loo = LeaveOneOut() 
    y_true, y_pred = [], [] 
    
        # Loop through each sample using LOOCV 
    for train_index, test_index in loo.split(X): 
        X_train, X_test = X.iloc[train_index], X.iloc[test_index] 
        y_train, y_test = y.iloc[train_index], y.iloc[test_index] 
        
                # Initialize and train the model 
        model = LinearRegression() 
        model.fit(X_train, y_train) 
        
                # Make prediction for the single test sample 
        y_pred.append(model.predict(X_test)[0]) 
        y_true.append(y_test.iloc[0]) 
        
            # Display metrics 
        display_metrics(y_true, y_pred) 
    
# K-Fold Cross-Validation Approach 
def kfold_approach(X, y, k=5): 
    print(f"{k}-Fold Cross-Validation Approach:") 

    
    kf = KFold(n_splits=k, shuffle=True, random_state=42) 
    y_true, y_pred = [], [] 
    
        # Loop through each fold 
    for train_index, test_index in kf.split(X): 
        X_train, X_test = X.iloc[train_index], X.iloc[test_index] 
        y_train, y_test = y.iloc[train_index], y.iloc[test_index] 
        
                # Initialize and train the model 
        model = LinearRegression() 
        model.fit(X_train, y_train) 
        
                # Make predictions on the test set 
        y_pred.extend(model.predict(X_test)) 
        y_true.extend(y_test) 
        
        # Display metrics 
        display_metrics(y_true, y_pred) 
    
# Main function to run all approaches 
def main(): 
    print("Cross-Validation for RMSE, MAE, and R²:\n") 
    validation_set_approach(X, y) 
    print("\n") 
    loocv_approach(X, y) 
    print("\n") 
    kfold_approach(X, y, k=5)  # You can change k for different K-Fold Cross-Validation 
    
    # Execute the main function 

if __name__ == "__main__": 
    main()