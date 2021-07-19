import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 22})

#Set parameters
h = 1
v_x = 0
v_y = 0
R = 1

#Constants
a = -9.81
dt = 0.001
endTime = 20

x_circ = np.linspace(-R, R, 100)
y_circ = np.sqrt(R**2-x_circ**2)

d_arr = np.logspace(-10, -0.01, num=int(1e3))
bounces_arr = np.ones(d_arr.shape[0])

for i, d in enumerate(d_arr):

    v_x = 0
    v_y = 0
    bounces = 0

    s_x = d
    s_y = R + h

    x_arr = np.zeros(int(endTime/dt - 1))
    y_arr = np.zeros(int(endTime/dt - 1))

    for j, t in enumerate(np.arange(dt, endTime, dt)):
        s_y = s_y + v_y*dt + 0.5*a*dt**2
        v_y = v_y + a*dt

        s_x = s_x + v_x*dt

        if(s_x**2+s_y**2<R):
            theta = np.arctan2(s_x, s_y)
            v = np.sqrt(v_x**2 + v_y**2)
            v_y = v*np.cos(2*theta)
            v_x = v*np.sin(2*theta)
            bounces = bounces + 1

        x_arr[j] = s_x
        y_arr[j] = s_y
    
    if i == 10:
        plt.figure()
        plt.axis('scaled')
        plt.xlim(-R, h+R)
        plt.ylim(-R, h+R)

        plt.plot(x_circ, y_circ, 'r', linewidth=5)
        plt.plot(x_circ, -y_circ, 'r', linewidth=5)

        plt.plot(x_arr, y_arr, 'b.')
        
    bounces_arr[i] = bounces

    if(bounces==1):
        break

plt.figure()
plt.plot(d_arr, bounces_arr, 'b.')
plt.xlabel("$d/R$")
plt.ylabel("$b(d)$")
plt.title("Simulation of Bounces")

plt.plot(d_arr, np.ceil(-np.log10(d_arr)), 'r.', alpha=0.5)

# plt.figure()
# plt.plot(d_arr, bounces_arr)

# plt.figure()
# plt.bar(d_arr, bounces_arr, width=d_stepsize)

# for k in np.unique(bounces_arr):
#     for l in range(bounces_arr.shape[0]):
#         if(bounces_arr[l] == k):
#             print("%d bounce at d = %.4f" % (k, d_arr[l]))
#             break

plt.show()