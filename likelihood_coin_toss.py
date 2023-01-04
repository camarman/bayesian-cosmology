# For a coin toss example (Binomial Dist.) plotting the likelihood Function
# and calculating the Most Likelihood parameter

from math import factorial

from matplotlib import pyplot as plt
from numpy import arange
from numpy import log as ln


def combination(n, r):
    """Calculating the Combination of n

    Args:
        n (int): total number of objects in the set
        r (int): number of choosing objects from the set


    Returns:
        [int] : the result of the combination
    """
    return factorial(n) / (factorial(r) * factorial(n-r))


def binomial_dist(n, r, theta):
    """
    The Liklihood Function of the coin toss
    Args:
        n (int): Number of tosses
        r (int): Obtained heads in these tosses
        theta (float): The probability of obtaining heads given the data/the parameter of the model

    Returns:
        [int]: The likelihood function in terms of theta
    """
    return combination(n, r) * theta**r * (1 - theta)**(n-r)


# Theta parameter for the binomial distribution
theta_test = arange(0.1, 1, 10**(-2))

# Likelihood as a function of theta for a given n and r.
L = binomial_dist(n = 6, r = 2, theta = theta_test)

#Taking the logarithm of the Likelihood
logL = ln(L)


data_points = dict(zip(logL, theta_test))

# maximum likelihood of theta
MLE_theta = data_points[max(logL)]  
print("theta_MLE =", round(MLE_theta, 4))

plt.plot(theta_test, logL)
plt.xlabel("$\\theta$")
plt.ylabel("$L(\\theta | \hat{x})$")
plt.grid(True)
plt.show()
