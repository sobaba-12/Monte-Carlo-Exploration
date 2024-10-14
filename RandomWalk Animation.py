import matplotlib.pyplot as plt
import random as rand
import numpy as np
import matplotlib.animation as animation

def randWalk3D(N, seed=None):
    rand.seed(seed)

    x = np.zeros(N+1)
    y = np.zeros(N+1)
    z = np.zeros(N+1)
    dxArr = []
    dyArr = []
    dzArr = []
    
    R_rms = 0
    for i in range(1,N+1):
        dx_prime = (rand.random() - 0.5)*2
        dy_prime = (rand.random() - 0.5)*2
        dz_prime = (rand.random() - 0.5)*2
        norm = 1#1/(np.sqrt(dx_prime**2+dy_prime**2+dz_prime**2))
        dx = norm*dx_prime
        dy = norm*dy_prime
        dz = norm*dz_prime
        dxArr.append(dx)
        dyArr.append(dy)
        dzArr.append(dz)
        x[i] = x[i-1] + dx
        y[i] = y[i-1] + dy
        z[i] = z[i-1] + dz
        R_rms += (dx**2+dy**2+dz**2)
    dxArr = np.array(dxArr)
    dyArr = np.array(dyArr)
    dzArr = np.array(dzArr)
    R_rms = np.sqrt(R_rms)
    
    return x,y,z,dxArr,dyArr,dzArr,R_rms

def randWalk(N, seed=None):
    rand.seed(seed)

    x = np.zeros(N+1)
    y = np.zeros(N+1)
    dxArr = []
    dyArr = []
    
    R_rms = 0
    for i in range(1,N+1):
        dx_prime = (rand.random() - 0.5)*2
        dy_prime = (rand.random() - 0.5)*2
        norm = 1/(np.sqrt(dx_prime**2+dy_prime**2))
        dx = norm*dx_prime
        dy = norm*dy_prime
        dxArr.append(dx)
        dyArr.append(dy)
        x[i] = x[i-1] + dx
        y[i] = y[i-1] + dy
        R_rms += (dx**2+dy**2)
    dxArr = np.array(dxArr)
    dyArr = np.array(dyArr)
    R_rms = np.sqrt(R_rms)
    
    return x,y,dxArr,dyArr,R_rms

userInput = "2"
if userInput == "1":
    fig, ax = plt.subplots()
    N = 5000
    artists = []
    x, y = randWalk(N)[0:1]
    for i in range(N):
        container = ax.plot(x[:i], y[:i], 'b')
        artists.append(container)

    ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=10)
    plt.show()
else:
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    N = 1000
    artists = []
    x,y,z = randWalk3D(N)[0:3]
    for i in range(N):
        container = ax.plot(x[:i],y[:i],z[:i], 'g')
        artists.append(container)
    ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=10)
    plt.show()