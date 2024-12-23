# Import necessary libraries 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

 
import seaborn as sns 
from sklearn.datasets import load_iris 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
from sklearn.preprocessing import StandardScaler 
 
# Load the Iris dataset 
data = load_iris() 
X = data.data  # Features 
y = data.target  # Target variable (0, 1, 2) 
target_names = data.target_names  # Class names 
 
# Standardize the data (LDA benefits from scaling) 
scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 
 
# Apply Linear Discriminant Analysis (LDA) 
lda = LinearDiscriminantAnalysis(n_components=2)  # Reduce to 2 components for visualization 
X_lda = lda.fit_transform(X_scaled, y) 
 
# Create a DataFrame for LDA-transformed data 
lda_df = pd.DataFrame(X_lda, columns=['LDA1', 'LDA2']) 
lda_df['Target'] = y 
 
# Plot the LDA results in 2D space 
plt.figure(figsize=(8, 6)) 
sns.scatterplot(data=lda_df, x='LDA1', y='LDA2', hue='Target', palette='Set1', style='Target', 
s=100) 
plt.title('LDA of Iris Dataset') 
plt.xlabel('Linear Discriminant 1') 

 
plt.ylabel('Linear Discriminant 2') 
plt.legend(title='Class', labels=target_names) 
plt.grid() 
plt.show() 
 
# Print key insights 
print("Linear Discriminant Analysis (LDA) Results") 
print("--------------------------------------------------") 
print("Explained Variance Ratio by LDA Components:") 
for i, ratio in enumerate(lda.explained_variance_ratio_, start=1): 
    print(f"  LDA{i}: {ratio:.4f}") 