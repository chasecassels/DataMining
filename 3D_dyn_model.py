import numpy as np
import matplotlib.pyplot as plt

#fixed points: ( ±sqrt(b(r-1)), ±sqrt(b(r-1)), r-1 )

def f(t, x):
    x, y, z = x
    s = 10 # s = sigma
    b = 8/3
    r = 28
    dxdt = s*(y-x)
    dydt = (r*x) - (x*z) - y
    dzdt = (x*y) - (b*z)
    return np.array([dxdt, dydt, dzdt])

def rk4(t0, x0, h, num_steps):
    t = t0
    x = x0
    
    t_values = [t]
    x_values = [x[0]]
    y_values = [x[1]]
    z_values = [x[2]]
    
    for _ in range(num_steps):
        k1 = h * f(t, x)
        k2 = h * f(t + 0.5 * h, x + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, x + 0.5 * k2)
        k4 = h * f(t + h, x + k3)
        x = x + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        t = t + h
        t_values.append(t)
        x_values.append(x[0])
        y_values.append(x[1])
        z_values.append(x[2])
    return t_values, x_values, y_values, z_values

t0 = 0
h = 0.01

x0 = np.array([1,1,1])
t_values, x_values, y_values, z_values = rk4(t0, x0, h, 5000)

#plt.plot(x_values[2500:], y_values[2500:])
#fig, axs = plt.subplots(2)
#axs[0].plot(t_values, x_values)
#axs[1].plot(t_values, y_values)
#ax = plt.gca()

fig = plt.figure()  
ax = fig.add_subplot(projection='3d')  
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z') 
ax.plot(x_values, y_values, z_values) 
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_zlim(0, 60)

plt.show()



