""" Patient's inflammation analysis for day 1 """

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='data/inflammation1.csv', delimiter=',')

#Finding dimentions of data
print(data.shape)

print(data)

#Print jusr the first row of data getting day1 data
print(data[0])

#plotting data
image-1=plt.plot(data)

plt.show(image-1)

