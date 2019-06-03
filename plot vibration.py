import scipy.fftpack
import json
import numpy as np
import math
from matplotlib import pyplot as plt
import scipy.fftpack

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]



y = np.array([])
x = np.array([])

f =open('ang.log')
lines = f.readlines()
for line in lines:
        q1 = json.loads(line)
        #print(y["payload"])
        #x = np.append(x,int(q1["time"])-1559194679879)
        k = q1["payload"].split("\"")
        y = np.append(y,int(k[0]))
        #print("hi")
        #print(y)


n = y.size
timestep = 1/100
freq = np.fft.fftfreq(n, d=timestep)
yf = scipy.fftpack.fft(y)
#print(freq)
xf = np.linspace(0.0, 1.0/(2.0*timestep), n/2)
plt.plot(xf,(2/n)*abs(yf[:n//2]))
fsize = freq.size
nval = find_nearest(xf,500)
print(nval)
print(yf.size)
plt.show()



