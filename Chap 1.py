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
###
trials = 4000
hits = simulate_number_of_hits(trials)
print(hits , "hits, estimate of pi =", 4 * hits / trials )
###
def random_in_disk():
    """Returns a uniform point in the unit disk via rejection."""
    position = random_in_square()
    while not is_in_circle(position):
        position = random_in_square()
    return position

# let us test this visually
# sample 500 points in NumPy array
testpoints = np.array([random_in_disk() for i in range(500)])
# make a plot
fig, ax = plt.subplots()  
ax.set_xlim(-1,1)    # set axis limits
ax.set_ylim(-1,1)
ax.set_aspect('equal')    # preserve aspect ratio of the circle
ax.add_patch(plt.Circle((0,0),1.0,edgecolor='gray',facecolor='none'))
plt.scatter(testpoints[:,0],testpoints[:,1],s=2)
plt.show()
###
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
###
trials = 40000
delta = 0.3
start = np.array([1,1])  # top-right corner
hits = naive_markov_pebble(start,delta,trials)
print(hits , "hits out of", trials, ", naive estimate of pi =", 4 * hits / trials )
###
def naive_markov_pebble_generator(start,delta,N):
    """Same as naive_markov_pebble but only yields the positions."""
    position = start
    for i in range(N):
        position = sample_next_position_naively(position,delta)
        yield position

# collect an array of points
trials = 40000
delta = 0.4
start = np.array([1,1])
testpoints = np.array(list(naive_markov_pebble_generator(start,delta,trials)))

# make a plot
fig, ax = plt.subplots() 
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_aspect('equal') # preserve aspect ratio of the square
plt.hist2d(testpoints[:,0],testpoints[:,1], bins=10, vmin=0)
plt.colorbar()
plt.show()
###
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

trials = 40000
delta = 0.3
start = [1,1]
hits = markov_pebble(start,delta,trials)
print(hits , "hits out of", trials, ", estimate of pi =", 4 * hits / trials )
###
def markov_pebble_generator(start,delta,N):
    """Same as markov_pebble but only yields the positions."""
    position = start
    for i in range(N):
        position = sample_next_position(position,delta)
        yield position

# collect an array of points
trials = 40000
delta = 0.4
start = np.array([1,1])
testpoints = np.array(list(markov_pebble_generator(start,delta,trials)))

# make a plot
fig, ax = plt.subplots() 
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_aspect('equal') # preserve aspect ratio of the square
plt.hist2d(testpoints[:,0],testpoints[:,1], bins=10, vmin=0)
plt.colorbar()
plt.show()
###
def simulate_discrete_pebble(m,N):
    """Simulate discrete pebble game of N moves on m sites, 
    returning a histogram of pebbles per site."""
    histogram = np.zeros(m, dtype=int)
    position = 0
    for i in range(N):
        position += np.random.choice([-1,1])
        position = max(position, 0)
        position = min(position, m-1)
        histogram[position] += 1
    return histogram

histogram = simulate_discrete_pebble(6,100000)
print(histogram)
plt.bar(range(6),histogram)
plt.show()