# Example 7 Part a - Coin Tossing

import numpy as np

from math import factorial
from matplotlib import pyplot as plt


def combination(n, r):
    '''
    Calculating the combination of (n,r)

    Args:
        n (int): total number of objects in the set
        r (int): number of choosing objects from the set
    '''
    return factorial(n) / (factorial(r)*factorial(n-r))


def likelihood(n, r, theta):
    '''
    The likelihood function for coin tossing

    Args:
        n (int): total number of tosses
        r (int): obtained heads in these tosses
        theta (float): the probability of obtaining heads
    '''
    return combination(n, r)*theta**r*(1 - theta)**(n-r)


# The range of the theta parameter
theta_test = np.arange(0, 1, 10**(-2))

# The likelihood function for a given n and r
L = likelihood(n=5, r=1, theta=theta_test)

# maximum likelihood for L
data_points = dict(zip(L, theta_test))
theta_ML = data_points[max(L)]
print('theta_ML = {}'.format(round(theta_ML, 4)))

plt.plot(theta_test, L, label='$n=5, r=1$')
plt.xlim([0, 1])
plt.xlabel(r'$\theta$')
plt.ylabel(r'$L(\theta)$')
plt.grid(True)
plt.legend()
plt.show()
