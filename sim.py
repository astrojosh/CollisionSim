import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 22})

# Create a shape to collide with the ball
# Possible options are "Circle" and "Ellipse"
class Shape:
    
    param1 = 0
    param2 = 0
    max_limit = 0
    x_range = []

    def __init__(self, shape):
        self.shape = shape

    def gen_range(self, data_points=100):
        self.x_range = np.linspace(-self.max_limit, self.max_limit, data_points)

    def get_range(self):
        return self.x_range

    def eq(self, range):
        if self.shape == "Circle":
            return np.sqrt(self.param1**2 - range**2)
        elif self.shape == "Ellipse":
            return self.param2 * np.sqrt(1 - (range / self.param1)**2)

    def within_shape(self, x, y):
        if x > self.max_limit:
            return False
        else:
            return y < self.eq(x)

    def set_radius(self, R):
        if self.shape == "Circle":
            self.param1 = R
            self.max_limit = R
        else:
            print("Can not set radius of non-circular shape")

    def set_ellipse_axis(self, a, b):
        if self.shape == "Ellipse":
            self.param1 = a
            self.param2 = b
            self.max_limit = np.max([a, b])
        else:
            print("Can not set radius of non-elliptical shape")

def gen_circle(radius):
    collider = Shape("Circle")
    collider.set_radius(radius)
    return collider

def gen_ellipse(axis1, axis2):
    collider = Shape("Ellipse")
    collider.set_ellipse_axis(axis1, axis2)
    return collider

def shape_coords(collider, data_points=100):
    collider.gen_range(data_points)
    x = collider.get_range()
    y = collider.eq(x)
    return x, y

def plot_shape(x, y):
    max_x = np.max(np.abs(x))
    max_y = np.max(np.abs(y))

    plt.figure()
    plt.axis('scaled')
    plt.xlim(-max_x, 1.1*h+max_x)
    plt.ylim(-max_y, 1.1*h+max_y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Simulation of Bounces")

    plt.plot(x, y, 'r', linewidth=5)
    plt.plot(x, -y, 'r', linewidth=5)

def simulate_bounces(collider, h, d, v_x, v_y):

    # Simulation properties
    a = -9.81
    dt = 0.001
    endTime = 20

    s_x = d
    s_y = collider.eq(d) + h

    n = int(endTime/dt)
    x_arr = np.zeros(n)
    y_arr = np.zeros(n)

    for i in range(n):
        s_y = s_y + v_y * dt + 0.5 * a * dt**2
        v_y = v_y + a * dt

        s_x = s_x + v_x * dt

        if collider.within_shape(s_x, s_y):
            theta = np.arctan2(s_x, s_y)
            v = np.sqrt(v_x**2 + v_y**2)
            v_y = v * np.cos(2 * theta)
            v_x = v * np.sin(2 * theta)
            print(f"Bounce! \n s_x = {s_x} \n v = {v}\n")

        x_arr[i] = s_x
        y_arr[i] = s_y

    return x_arr, y_arr

def plot_bounces(x, y):
    plt.plot(x, y, 'b.')
    plt.show()

if __name__ == "__main__":

    # Radius of circle
    r = 1
    # Height above surface where object is dropped
    h = 1
    # Horizontal distance where object is dropped
    d = 0.09
    # Initial horizontal velocity of object
    v_x = 0
    # Initial vertical velocity of object
    v_y = 0

    collider = gen_circle(r)
    x_circ, y_circ = shape_coords(collider)
    plot_shape(x_circ, y_circ)
    x, y = simulate_bounces(collider, h, d, v_x, v_y)
    plot_bounces(x, y)

    # collider = gen_ellipse(2, 1)
    # x_ell, y_ell = shape_coords(collider, data_points=1000)
    # plot_shape(x_ell, y_ell)
    # x, y = simulate_bounces(collider, h, d, v_x, v_y)
    # plot_bounces(x, y)