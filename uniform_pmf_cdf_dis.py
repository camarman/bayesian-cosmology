# Creating a uniform distribution as probability mass function (PMF) for a given interval
# Calculating the cumulative probability distribution function (CDF)

from random import randint

from matplotlib import pyplot as plt
from numpy import arange, histogram


def CDF_calculator(norm_freq_array):
    """Calculating the CDF distribution for each probability

    Args:
        norm_freq_array (list)): normalized distribution of the frequency of the data

    Returns:
        [array]: An array of values that gives the reuslt of the CDF
    """
    data = []
    for i in range(len(norm_freq_array)+1):
        data.append(sum(norm_freq_array[0:i]))
    return data[1:]


# minimum and maximum values of the given uniform distributions
min_val, max_val = 3, 10

# Possible outcomes; 1,2,3...n
r_values = arange(min_val, max_val+1)

# Number of experiments
N = 10**5


# The probability of getting each value from a random selection
print("P(r) =", 1 / len(r_values))

# Our sample space
sample_space = [randint(min_val, max_val) for i in range(N)]

P_r_freq, P_r_bins = histogram(sample_space, bins=len(r_values))

# Calculating P(r) for N experiments (Normalizing the probability to 1)
P_r_freq_norm = P_r_freq / N

# Plotting r vs P(r)
plt.bar(r_values, P_r_freq_norm, width=0.5)
plt.xlabel("$r$")
plt.ylabel("$P(r)$")
plt.title("Uniform PMF")
plt.show()

CDF_dist = CDF_calculator(P_r_freq_norm)

# Plotting r vs P(X < r)
plt.bar(r_values, CDF_dist, width=0.5)
plt.xlabel("$r$")
plt.ylabel("$P(X < r)$")
plt.title("Uniform CDF")
plt.show()
