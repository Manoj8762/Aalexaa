# Import necessary libraries 
import numpy as np 
import pandas as pd 
from scipy import stats 
 
# Sample data for demonstration 
# One-sample test: A group of exam scores 
exam_scores = np.array([85, 87, 90, 78, 88, 95, 82, 79, 94, 91]) 
 
# Two-sample test: Scores of two different groups 
group_A = np.array([85, 89, 88, 90, 93, 85, 84, 79, 90, 87]) 
group_B = np.array([82, 86, 85, 87, 92, 80, 81, 78, 89, 85]) 
 
# Paired-sample test: Before and after treatment scores of the same group 
before_treatment = np.array([82, 84, 88, 78, 80, 85, 90, 79, 87, 83]) 
after_treatment = np.array([85, 87, 89, 81, 83, 88, 92, 82, 89, 86]) 
 
# Function to perform one-sample t-test 
def one_sample_ttest(data, population_mean): 
    t_stat, p_value = stats.ttest_1samp(data, population_mean) 
    return t_stat, p_value 
 
# Function to perform two-sample t-test (independent samples) 
def two_sample_ttest(group1, group2): 
    t_stat, p_value = stats.ttest_ind(group1, group2) 
    return t_stat, p_value 
    

# Function to perform paired-sample t-test 
def paired_sample_ttest(before, after): 
    t_stat, p_value = stats.ttest_rel(before, after) 
    return t_stat, p_value 
 
# Analyze results of the t-tests 
def analyze_ttest_results(t_stat, p_value, alpha=0.05): 
    print(f"T-statistic: {t_stat}") 
    print(f"P-value: {p_value}") 
    if p_value < alpha : 
        print("Result: The null hypothesis is rejected (statistically significant difference).") 
    else: 
        print("Result: The null hypothesis cannot be rejected (no statistically significant  difference).") 
        
# One-sample t-test: Compare exam scores with a population mean (e.g., 85) 
print("One-Sample T-Test:") 
t_stat, p_value = one_sample_ttest(exam_scores, 85) 
analyze_ttest_results(t_stat, p_value) 
print() 
 
# Two-sample t-test: Compare the means of two independent groups 
print("Two-Sample T-Test:") 
t_stat, p_value = two_sample_ttest(group_A, group_B) 
analyze_ttest_results(t_stat, p_value) 
print() 
 
# Paired-sample t-test: Compare before and after treatment of the same group 
print("Paired-Sample T-Test:") 
t_stat, p_value = paired_sample_ttest(before_treatment, after_treatment) 

 
analyze_ttest_results(t_stat, p_value)