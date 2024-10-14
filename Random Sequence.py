import random as rand
import numpy as np
import matplotlib.pyplot as plt

def lin_cong(a, c, M, r1):
    seq = [r1]
    i = 0
    ri = (a*seq[i]+c)%M
    period = 0
    while ri != r1:
        ri = (a*seq[i]+c)%M
        seq.append(ri)
        period += 1
        i += 1
    return seq, period

master = lin_cong(57,1,256,10)[0]
x = np.array(master[0::2][:-1])
y = np.array(master[1::2])
rand_lst = []
for i in range(len(master)):
    rand_lst.append(rand.randint(0,255))


fig, ax = plt.subplots()
# Plots the sequence pattern
#ax.plot(x,y,'r.')

# Comparison between random and lin_cong, with unreasonable parameters
ax.plot(np.arange(0,len(master)), np.array(master), '-o')
ax.plot(np.arange(0,len(master)), np.array(rand_lst), '-o')
plt.show()