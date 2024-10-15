import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pylab as plt
from nose.tools import assert_almost_equal
from Chap1Functions import *

rng = np.random.default_rng()



def pi_stddev(n,m):
    """Estimate the standard deviation in the pi estimate in the case of n trials,
    based on m runs of the direct-sampling pebble game."""
    results = []
    trials = n
    for i in range(m):
        hits = simulate_number_of_hits(trials)
        pi = 4*hits/trials
        results.append(pi)
    std = np.std(results, ddof=1)
    return std

def fit_power_law(stddev_data):
    """Compute the best fit parameters a and p."""
    func = lambda n,a,p: np.log(a) + p*np.log(n)
    log_sigma = np.log(stddev_data[:,1])
    popt, pcov = curve_fit(func, stddev_data[:,0], log_sigma)
    a_fit = popt[0]; p_fit = popt[1]
    return a_fit, p_fit

stddev_data = np.array([[2**k,pi_stddev(2**k,200)] for k in range(4,12)])
a,p = fit_power_law(stddev_data)
values = np.linspace(1,2**13)
sigma = a*values**p
fig, ax = plt.subplots()
plt.loglog()
ax.plot(stddev_data[:,0], stddev_data[:,1])
ax.plot(values,sigma)
plt.show()
