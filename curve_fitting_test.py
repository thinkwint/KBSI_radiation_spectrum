import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
from scipy.constants import h, k, c

# init wavelength (nm)
wl_min = 900
wl_max = 1700

# x = np.linspace(0.0000009, 0.0000017)  # wavelength range
x = np.linspace(wl_min / 1e9, wl_max / 1e9, 100)  # wavelength range

# init temperature in Celsius
# Temp_min = 600
# Temp_max = 1500
# step = 100


radiation_temp = 1200
Temp_Kelvin = 273.

radiation_temp_K = radiation_temp + Temp_Kelvin

# temperature in Kelvin
# Temp_min_K = Temp_min + Temp_Kelvin
# Temp_max_K = Temp_max + Temp_Kelvin

# Temp_step = int(((Temp_max - Temp_min) / step) + 1)
# T = 400  # temperature (K)
# T = np.linspace(Temp_min_K, Temp_max_K, Temp_step)  # temperature (K)
# w = np.empty((len(T), 50))
# lw = np.empty((len(T), 50))


def planck_curve(wl, tr):  # function of Planck's law
    c1 = 2 * np.pi * h * (c ** 2)
    # c1 = 2 * h * (c ** 2)
    return c1 / ((wl ** 5) * (np.exp((h * c) / (k * wl * tr)) - 1))


w = planck_curve(x, radiation_temp_K)
noise = np.random.randn(len(x)) * 2e9
y_noise = w + noise

popt, pcov = curve_fit(planck_curve, x, y_noise, p0 = 1000)

estimated_temp = popt - Temp_Kelvin
print('inital temperature %d' % radiation_temp)
print('estimated temperature %.2f' % estimated_temp)
# print(popt, pcov)

y_fit = planck_curve(x, popt)

plt.plot(x, y_fit, label=popt, linestyle='--')
plt.plot(x, w)
plt.plot(x, y_noise)
plt.show()
