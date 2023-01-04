# Example 7 Part b - Coin Tossing

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
L_1 = likelihood(n=5, r=1, theta=theta_test)
L_2 = likelihood(n=5, r=2, theta=theta_test)
L_3 = likelihood(n=5, r=3, theta=theta_test)
L_4 = likelihood(n=5, r=4, theta=theta_test)
L_5 = likelihood(n=5, r=5, theta=theta_test)

# maximum likelihood for L1
data_points_1 = dict(zip(L_1, theta_test))
theta_1_ML = data_points_1[max(L_1)]
print('theta_1_ML = {}'.format(round(theta_1_ML, 4)))

# maximum likelihood for L2
data_points_2 = dict(zip(L_2, theta_test))
theta_2_ML = data_points_2[max(L_2)]
print('theta_2_ML = {}'.format(round(theta_2_ML, 4)))

# maximum likelihood for L3
data_points_3 = dict(zip(L_3, theta_test))
theta_3_ML = data_points_3[max(L_3)]
print('theta_3_ML = {}'.format(round(theta_3_ML, 4)))

# maximum likelihood for L4
data_points_4 = dict(zip(L_4, theta_test))
theta_4_ML = data_points_4[max(L_4)]
print('theta_4_ML = {}'.format(round(theta_4_ML, 4)))

# maximum likelihood for L5
data_points_5 = dict(zip(L_5, theta_test))
theta_5_ML = data_points_5[max(L_5)]
print('theta_5_ML = {}'.format(round(theta_5_ML, 4)))

plt.plot(theta_test, L_1, color='red',    label='$n=5, r=1$')
plt.plot(theta_test, L_2, color='blue',   label='$n=5, r=2$')
plt.plot(theta_test, L_3, color='orange', label='$n=5, r=3$')
plt.plot(theta_test, L_4, color='purple', label='$n=5, r=4$')
plt.plot(theta_test, L_5, color='yellow', label='$n=5, r=5$')

plt.xlim([0, 1])
plt.xlabel(r'$\theta$')
plt.ylabel(r'$L(\theta)$')
plt.grid(True)
plt.legend()
plt.show()
