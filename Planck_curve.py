import matplotlib.pyplot as plt
import numpy as np


from scipy.constants import h, c, k

print(h, k, c, np.pi)
print('radiation spectrum')
min_wl = 900e-9
max_wl = 1700e-9
x = np.linspace(min_wl, max_wl)

t = 1200
t_K = 1200 + 273


def plank_curve(wl, t):
    return (2 * np.pi * h * c ** 2) / ((wl ** 5) * (np.exp(((h * c)/(k * wl * t)) - 1)))


y = plank_curve(x, t_K)
plt.plot(x, y)
plt.show()
