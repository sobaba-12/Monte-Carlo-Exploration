import random as rand
import numpy as np
import matplotlib.pyplot as plt

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

def compare(N,dx,dy,R_rms):
    err = []
    for i in range(1,N-1):
        ans = (dx[i]*dy[i+1])/(R_rms**2)
        err.append(ans)
    return max(err), min(err)

userInput = "3"
if userInput == "1":
    fig, ax = plt.subplots()
    mean = 0
    bigM = 0
    smallM = 0
    N = 500
    K = int(np.sqrt(N))
    for i in range(K):
        x,y,dx,dy,R = randWalk(N)
        big, small = compare(N,dx,dy,R)
        R = R**2
        ax.plot(x,y)
        mean += 1/K*R
        bigM += 1/K*big
        smallM += 1/K*small
    print(mean, bigM, smallM)
    plt.show()
elif userInput == '2':
    fig, ax = plt.subplots()
    N = 5000
    x,y,dx,dy,R = randWalk(N)
    big, small = compare(N,dx,dy,R)
    R = R**2
    ax.plot(x,y)
    print(R, big, small)
    plt.show()
else:
    fig, axs = plt.subplots(1,2)
    N = np.sqrt(np.arange(1,5001))
    R_rms = np.zeros(5000)
    for i in range(5000):
        R_rms[i] = randWalk(i, seed=1)[4]
    x,y,dx,dy,R = randWalk(5000, seed=1)
    axs[0].plot(x,y)
    # Model
    R = 1
    model = R*N
    axs[1].plot(N,model)
    axs[1].plot(N,R_rms)
    plt.show()