import matplotlib.pyplot as plt
import numpy as np
import random as rand
import winsound

def decay(N, lam):
    t = 0
    x = [0]
    y1 = [N]
    y2 = [0]

    while N>1:
        dN = 0
        for i in range(1,N):
            if (rand.random() < lam):
                dN += 1
                winsound.Beep(600,100)
        t += 1
        x.append(t)
        N -= dN
        y1.append(N)
        y2.append(dN)
    return x,y1,y2

fig, axs = plt.subplot_mosaic([["ln num", "ln num", 'ln rate', 'ln rate'],
                               ['N0', 'N0', 'lambda', 'lambda'],
                               ['.','prop','prop','.']])
plt.yscale('log', base=np.e)
x,y1,y2 = decay(1000,0.5)
axs["ln num"].plot(x,y1)
axs["ln rate"].plot(x,y2)
plt.yscale('linear')
N = 1000
lam = 0.5
for i in range(3):
    x,y1,y2 = decay(N, lam)
    N += 100**i
N = 1000
for i in range(3):
    x, y1, y2 = decay(N,lam)
    axs['lambda'].plot(x, y2)
    lam -= 0.1
plt.xscale('log',base=np.e)
plt.yscale('log',base=np.e)
axs['prop'].plot(y1,y2)
plt.show()