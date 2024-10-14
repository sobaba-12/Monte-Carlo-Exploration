import random as rand
import numpy as np
import matplotlib.pyplot as plt

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

def compare3d(N,dx,dy,dz,R_rms):
    err = []
    for i in range(1,N-2):
        ans = (dx[i]*dy[i+1]*dz[i+2])/(R_rms**2)
        err.append(ans)
    return max(err), min(err)

userInput = "3"
if userInput == "1":
    ax = plt.figure().add_subplot(projection='3d')
    N = 500
    mean = 0
    bigM = 0
    smallM = 0
    K = int(np.sqrt(N))
    for i in range(K):
        x,y,z,dx,dy,dz,R = randWalk3D(N)
        big, small = compare3d(N,dx,dy,dz,R)
        R = R**2
        ax.plot(x,y,z)
        mean += 1/K*R
        bigM += 1/K*big
        smallM += 1/K*small
    print(mean, bigM, smallM)
    plt.show()
elif userInput == "2":
    ax = plt.figure().add_subplot(projection='3d')
    N = 5000
    x,y,z,dx,dy,dz,R = randWalk3D(N)
    big, small = compare3d(N,dx,dy,dz,R)
    R = R**2
    ax.plot(x,y,z)
    print(R, big, small)
    plt.show()
else:
    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax1 = fig.add_subplot(1,2,1, projection="3d")
    N = np.sqrt(np.arange(1,5001))
    R_rms = np.zeros(5000)
    for i in range(5000):
        R_rms[i] = randWalk3D(i, seed=10)[6]
    x,y,z,dx,dy,dz,R = randWalk3D(5000, seed=10)
    ax1.plot(x,y,z)
    # Model
    R = 1
    model = R*N
    ax2 = fig.add_subplot(1,2,2)
    ax2.plot(N,model)
    ax2.plot(N,R_rms)
    plt.show()