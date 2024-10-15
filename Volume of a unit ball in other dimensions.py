import numpy as np
from scipy.special import gamma
import matplotlib.pylab as plt
from nose.tools import assert_almost_equal
from Chap1Functions import *

def number_of_hits_in_d_dimensions(N,d):
    """Simulates number of hits in case of N trials in the d-dimensional direct-sampling pebble game."""
    number_hits = 0
    for i in range(N):
        position = rng.uniform(-1,1,d)
        if np.dot(position,position) < 1:
            number_hits += 1
    return number_hits

# rel_error = result - exact/exact
trials = 10_000
exact_vol = lambda d: np.pi**(d/2)/gamma((d/2)+1)
array = np.array([[exact_vol(d), (2**d)*(number_of_hits_in_d_dimensions(trials,d)/trials)] for d in range(1,8)])
rel_error = (array[:,1]-array[:,0])/array[:,0]
d = np.linspace(1,8,7)
fig,ax = plt.subplots()
ax.plot(d,rel_error)
plt.show()