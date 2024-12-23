# program -06
# Program to display Normal, Binomial Poisson, Bernoulli disrtibutions for a given frequency distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, bernoulli

def get_user_data():
    # Get the frequency distribution input from the user
    data_input = input("Enter the data values separated by commas (e.g., 10, 20, 30): ")
    frequencies_input = input("Enter the corresponding frequencies separated by commas (e.g., 2, 3, 4): ")
    
    # Convert the inputs into lists of integers
    data = list(map(int, data_input.split(',')))
    frequencies = list(map(int, frequencies_input.split(',')))
    
    return data, frequencies

def plot_normal_distribution(data, frequencies):
    # Fit and plot Normal distribution
    mean = np.mean(data)
    std_dev = np.std(data)
    
    x = np.linspace(min(data), max(data), 100)
    pdf = norm.pdf(x, mean, std_dev)

    plt.plot(x, pdf, 'r-', lw=2, label='Normal Distribution')
    plt.title('Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.show()

def plot_binomial_distribution(data, frequencies):
    # Fit and plot Binomial distribution (assuming n is max(data) and p is mean/len(data))
    n = max(data)
    p = np.mean(data) / n
    
    x = np.arange(0, n+1)
    pmf = binom.pmf(x, n, p)

    plt.bar(x, pmf, alpha=0.7, color='b', label='Binomial Distribution')
    plt.title('Binomial Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def plot_poisson_distribution(data, frequencies):
    # Fit and plot Poisson distribution (lambda is the mean of the data)
    lam = np.mean(data)
    
    x = np.arange(0, max(data)+1)
    pmf = poisson.pmf(x, lam)

    plt.bar(x, pmf, alpha=0.7, color='g', label='Poisson Distribution')
    plt.title('Poisson Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def plot_bernoulli_distribution(data, frequencies):
    # Assuming binary outcome for Bernoulli
    success_prob = np.mean(data) / max(data)
    
    x = [0, 1]
    pmf = bernoulli.pmf(x, success_prob)

    plt.bar(x, pmf, alpha=0.7, color='purple', label='Bernoulli Distribution')
    plt.title('Bernoulli Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def analyze_distributions(data, frequencies):
    print("Analyzing Normal Distribution:")
    plot_normal_distribution(data, frequencies)
    
    print("Analyzing Binomial Distribution:")
    plot_binomial_distribution(data, frequencies)
    
    print("Analyzing Poisson Distribution:")
    plot_poisson_distribution(data, frequencies)
    
    print("Analyzing Bernoulli Distribution:")
    plot_bernoulli_distribution(data, frequencies)

# Main program
data, frequencies = get_user_data()
analyze_distributions(data, frequencies)# program -06
# Program to display Normal, Binomial Poisson, Bernoulli disrtibutions for a given frequency distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, bernoulli

def get_user_data():
    # Get the frequency distribution input from the user
    data_input = input("Enter the data values separated by commas (e.g., 10, 20, 30): ")
    frequencies_input = input("Enter the corresponding frequencies separated by commas (e.g., 2, 3, 4): ")
    
    # Convert the inputs into lists of integers
    data = list(map(int, data_input.split(',')))
    frequencies = list(map(int, frequencies_input.split(',')))
    
    return data, frequencies

def plot_normal_distribution(data, frequencies):
    # Fit and plot Normal distribution
    mean = np.mean(data)
    std_dev = np.std(data)
    
    x = np.linspace(min(data), max(data), 100)
    pdf = norm.pdf(x, mean, std_dev)

    plt.plot(x, pdf, 'r-', lw=2, label='Normal Distribution')
    plt.title('Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.show()

def plot_binomial_distribution(data, frequencies):
    # Fit and plot Binomial distribution (assuming n is max(data) and p is mean/len(data))
    n = max(data)
    p = np.mean(data) / n
    
    x = np.arange(0, n+1)
    pmf = binom.pmf(x, n, p)

    plt.bar(x, pmf, alpha=0.7, color='b', label='Binomial Distribution')
    plt.title('Binomial Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def plot_poisson_distribution(data, frequencies):
    # Fit and plot Poisson distribution (lambda is the mean of the data)
    lam = np.mean(data)
    
    x = np.arange(0, max(data)+1)
    pmf = poisson.pmf(x, lam)

    plt.bar(x, pmf, alpha=0.7, color='g', label='Poisson Distribution')
    plt.title('Poisson Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def plot_bernoulli_distribution(data, frequencies):
    # Assuming binary outcome for Bernoulli
    success_prob = np.mean(data) / max(data)
    
    x = [0, 1]
    pmf = bernoulli.pmf(x, success_prob)

    plt.bar(x, pmf, alpha=0.7, color='purple', label='Bernoulli Distribution')
    plt.title('Bernoulli Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def analyze_distributions(data, frequencies):
    print("Analyzing Normal Distribution:")
    plot_normal_distribution(data, frequencies)
    
    print("Analyzing Binomial Distribution:")
    plot_binomial_distribution(data, frequencies)
    
    print("Analyzing Poisson Distribution:")
    plot_poisson_distribution(data, frequencies)
    
    print("Analyzing Bernoulli Distribution:")
    plot_bernoulli_distribution(data, frequencies)

# Main program
data, frequencies = get_user_data()
analyze_distributions(data, frequencies)# program -06
# Program to display Normal, Binomial Poisson, Bernoulli disrtibutions for a given frequency distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, bernoulli

def get_user_data():
    # Get the frequency distribution input from the user
    data_input = input("Enter the data values separated by commas (e.g., 10, 20, 30): ")
    frequencies_input = input("Enter the corresponding frequencies separated by commas (e.g., 2, 3, 4): ")
    
    # Convert the inputs into lists of integers
    data = list(map(int, data_input.split(',')))
    frequencies = list(map(int, frequencies_input.split(',')))
    
    return data, frequencies

def plot_normal_distribution(data, frequencies):
    # Fit and plot Normal distribution
    mean = np.mean(data)
    std_dev = np.std(data)
    
    x = np.linspace(min(data), max(data), 100)
    pdf = norm.pdf(x, mean, std_dev)

    plt.plot(x, pdf, 'r-', lw=2, label='Normal Distribution')
    plt.title('Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.show()

def plot_binomial_distribution(data, frequencies):
    # Fit and plot Binomial distribution (assuming n is max(data) and p is mean/len(data))
    n = max(data)
    p = np.mean(data) / n
    
    x = np.arange(0, n+1)
    pmf = binom.pmf(x, n, p)

    plt.bar(x, pmf, alpha=0.7, color='b', label='Binomial Distribution')
    plt.title('Binomial Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def plot_poisson_distribution(data, frequencies):
    # Fit and plot Poisson distribution (lambda is the mean of the data)
    lam = np.mean(data)
    
    x = np.arange(0, max(data)+1)
    pmf = poisson.pmf(x, lam)

    plt.bar(x, pmf, alpha=0.7, color='g', label='Poisson Distribution')
    plt.title('Poisson Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def plot_bernoulli_distribution(data, frequencies):
    # Assuming binary outcome for Bernoulli
    success_prob = np.mean(data) / max(data)
    
    x = [0, 1]
    pmf = bernoulli.pmf(x, success_prob)

    plt.bar(x, pmf, alpha=0.7, color='purple', label='Bernoulli Distribution')
    plt.title('Bernoulli Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

def analyze_distributions(data, frequencies):
    print("Analyzing Normal Distribution:")
    plot_normal_distribution(data, frequencies)
    
    print("Analyzing Binomial Distribution:")
    plot_binomial_distribution(data, frequencies)
    
    print("Analyzing Poisson Distribution:")
    plot_poisson_distribution(data, frequencies)
    
    print("Analyzing Bernoulli Distribution:")
    plot_bernoulli_distribution(data, frequencies)

# Main program
data, frequencies = get_user_data()
analyze_distributions(data, frequencies)