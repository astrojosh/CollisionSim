import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 22})

alpha = np.arange(0, 100, 1)

theta1 = np.zeros(alpha.shape[0])
theta2 = np.zeros(alpha.shape[0])
theta3 = np.zeros(alpha.shape[0])
theta4 = np.zeros(alpha.shape[0])
theta5 = np.zeros(alpha.shape[0])

for a in alpha:
    theta1[a] = (-4 - a + 4 * np.sqrt(1 + a)) / (8 - a)
    theta2[a] = (a * theta1[a]) / (8 + a - 8 * theta1[a] ** 2)
    theta3[a] = (a * theta2[a]) / (8 + a - 8 * theta2[a] ** 2)
    theta4[a] = (a * theta3[a]) / (8 + a - 8 * theta3[a] ** 2)
    theta5[a] = (a * theta4[a]) / (8 + a - 8 * theta4[a] ** 2)

print(theta1[1])
print(theta2[1])
print(theta3[1])
print(theta4[1])
print(theta5[1])

plt.figure()
plt.plot(alpha, theta1, "b.")
plt.xlabel("$\\alpha$")
plt.ylabel("$\\theta$ / rad")
plt.title("First Bounce Critical Point")


plt.figure()
plt.plot(alpha, theta1, "b.", label="1 Bounce")
plt.plot(alpha, theta2, "r.", label="2 Bounces")
plt.plot(alpha, theta3, "g.", label="3 Bounces")
plt.plot(alpha, theta4, "y.", label="4 Bounces")
plt.plot(alpha, theta5, "m.", label="5 Bounces")
plt.legend(loc="upper left")
plt.xlabel("$\\alpha$")
plt.ylabel("$\\theta_i$ / rad")
plt.title("Critical Points for Bounces")

d = np.logspace(-10, -0.01, num=int(1e5))
plt.figure()
plt.plot(d, np.ceil(-np.log10(d)), "b.")
plt.xlabel("$d/R$")
plt.ylabel("$b(d)$")
plt.title("Formula Approximation")

plt.show()
