import scipy.fftpack
import json
import numpy as np
import math
from matplotlib import pyplot as plt



y = np.array([])
x = np.array([])

count = 0
f =open('rxt.log')
lines = f.readlines()
for line in lines:
    count = count+1
    q1 = json.loads(line)
    #print(y["payload"])
    x = np.append(x,int(q1["time"])-1558424210948)
    y = np.append(y,int(q1["payload"]))


kax=0

ya1 = np.array([])
while kax<20:
    ya1 = np.append(ya1,kax%2)
    kax  = kax+1
count = 0
# Number of samplepoints
N = count
# sample spacing
yf = scipy.fftpack.fft(ya1)
fig, ax = plt.subplots()
ax.plot(np.abs(yf))
plt.show()
