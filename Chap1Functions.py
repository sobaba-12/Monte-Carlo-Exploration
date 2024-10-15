import numpy as np
import matplotlib.pyplot as plt
# we make a habit of using NumPy's pseudorandom number generator
rng = np.random.default_rng()

def random_in_square():
    """Returns a random position in the square [-1,1)x[-1,1)."""
    return rng.uniform(-1,1,2)  

def is_in_circle(x):
    return np.dot(x,x) < 1

def simulate_number_of_hits(N):
    """Simulates number of hits in case of N trials in the pebble game."""
    number_hits = 0
    for i in range(N):
        position = random_in_square()
        if is_in_circle(position):
            number_hits += 1
    return number_hits

def random_in_disk():
    """Returns a uniform point in the unit disk via rejection."""
    position = random_in_square()
    while not is_in_circle(position):
        position = random_in_square()
    return position

def is_in_square(x):
    """Returns True if x is in the square (-1,1)^2."""
    return np.abs(x[0]) < 1 and np.abs(x[1]) < 1
    
def sample_next_position_naively(position,delta):
    """Keep trying a throw until it ends up in the square."""
    while True:
        next_position = position + delta*random_in_disk()
        if is_in_square(next_position):
            return next_position
    
def naive_markov_pebble(start,delta,N):
    """Simulates the number of hits in the naive Markov-chain version 
    of the pebble game."""
    number_hits = 0
    position = start
    for i in range(N):
        position = sample_next_position_naively(position,delta)
        if is_in_circle(position):
            number_hits += 1
    return number_hits

def naive_markov_pebble_generator(start,delta,N):
    """Same as naive_markov_pebble but only yields the positions."""
    position = start
    for i in range(N):
        position = sample_next_position_naively(position,delta)
        yield position

def sample_next_position(position,delta):
    """Attempt a throw and reject when outside the square."""
    next_position = position + delta*random_in_disk()
    if is_in_square(next_position):
        return next_position  # accept!
    else:
        return position  # reject!

def markov_pebble(start,delta,N):
    """Simulates the number of hits in the proper Markov-chain version of the pebble game."""
    number_hits = 0
    position = start
    for i in range(N):
        position = sample_next_position(position,delta)
        if is_in_circle(position):
            number_hits += 1
    return number_hits

def markov_pebble_generator(start,delta,N):
    """Same as markov_pebble but only yields the positions."""
    position = start
    for i in range(N):
        position = sample_next_position(position,delta)
        yield position