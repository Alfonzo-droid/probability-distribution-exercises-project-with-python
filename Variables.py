
from scipy.stats import norm,uniform
import numpy as np


def dnorm(x, mean = 0, std = 1):
    result = norm.pdf(x, loc = mean, scale = std)

    return result

def pnorm(x, mean = 0, std = 1):
    
    
    result = norm.cdf(x = x, loc = mean, scale = std)

    return result

def qnorm(p, mean = 0, std = 1):
    
    result = norm.ppf(q = p, loc = mean, scale = std)

    return result

def rnorm(n, mean = 0, std = 1):
    
    result = norm.rvs(size = n, loc = mean, scale = std)

    return result

import matplotlib.pyplot as plt
np.random.seed(42)

mean = 0
std = 1
data = np.arange(-5, 5, 0.01)

pmf = dnorm(data, mean = mean, std = std)
cdf = pnorm(data, mean = mean, std = std)
ppf = qnorm(data, mean = mean, std = std)

fig, axis = plt.subplots(3, 1, figsize = (5, 7))

axis[0].plot(data, pmf, "r-")
axis[1].plot(data, cdf, "b-")
axis[2].plot(data, ppf, "g-")

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()


# Uniform
def dunif(x, low = 0, high = 1):
    result = uniform.pdf(x, loc = low, scale = (high - low))

    return result

def punif(q, low = 0, high = 1):
    result = uniform.cdf(q, loc = low, scale = (high - low))

    return result

def qunif(p, low = 0, high = 1):
    result = uniform.ppf(p, loc = low, scale = (high - low))

    return result

def runif(n, low = 0, high = 1):
    
    result = uniform.rvs(loc = low, scale = (high - low), size = n)

    return result

np.random.seed(42)

low = 0
high = 1
data = np.arange(-5, 5, 0.01)

pmf = dunif(data, low = low, high = high)
cdf = punif(data, low = low, high = high)
ppf = qunif(data, low = low, high = high)

fig, axis = plt.subplots(3, 1, figsize = (5, 7))

axis[0].plot(data, pmf, "r-")
axis[1].plot(data, cdf, "b-")
axis[2].plot(data, ppf, "g-")

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()