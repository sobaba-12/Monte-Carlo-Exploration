import numpy as np
import matplotlib.pylab as plt
from nose.tools import assert_almost_equal
from Chap1Functions import *

trials = 2000
deltas = np.linspace(0,3,100)
pi_estimates = np.array([4*markov_pebble([1,1],deltas[i],trials)/trials for i in range(100)])
pi = np.pi*np.ones(100)
results = (pi_estimates-pi)**2
mean = np.mean(results)
print(mean)