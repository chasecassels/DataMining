import numpy as np
import matplotlib.pyplot as plt

r=0
x_values = []
r_values = []

for r in np.arange(-10,10,0.01):
    x = np.random.random()
    for i in range(1000):
        x = r*(np.cos(x))
        #only keep latter 600 values to ignore transient behaviour
        if i > 400:
            x_values.append(x)
            r_values.append(r)
    
plt.scatter(r_values, x_values, s=0.01)
plt.xlabel('r')
plt.ylabel('x')
plt.show()
