import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import h, k, c

# init wavelength (nm)
wl_min = 900
wl_max = 1700

# x = np.linspace(0.0000009, 0.0000017)  # wavelength range
x = np.linspace(wl_min / 1e9, wl_max / 1e9)  # wavelength range

# init temperature in Celsius
Temp_min = 600
Temp_max = 1500
step = 100
Temp_Kelvin = 273

# temperature in Kelvin
Temp_min_K = Temp_min + Temp_Kelvin
Temp_max_K = Temp_max + Temp_Kelvin

Temp_step = int(((Temp_max - Temp_min) / step) + 1)
# T = 400  # temperature (K)
T = np.linspace(Temp_min_K, Temp_max_K, Temp_step)  # temperature (K)
w = np.empty((len(T), 50))
# lw = np.empty((len(T), 50))


def planck_curve(wl, tr):  # function of Planck's law
    c1 = 2 * np.pi * h * (c ** 2)
    # c1 = 2 * h * (c ** 2)
    return c1 / ((wl ** 5) * (np.exp((h * c) / (k * wl * tr)) - 1))


# for i in range(0, len(T)):
for i in range(len(T)):
    w[i] = planck_curve(x, T[i])
    # lw[i] = np.log(w[i])  # log
    print(w[i])
    print(T[i])
    # print(i)

    plt.figure(1)  # Planck's curve in log scale
    plt.yscale("log")
    # plt.semilogy(x, w[i])
    plt.xlabel('wavelength')
    plt.ylabel('power density (log)')
    if i % 2 == 1:
        plt.plot(x, w[i], label=f"{int(T[i])}K ({int(T[i]) - Temp_Kelvin}$^\circ C$)", linestyle='--')
    else:
        plt.plot(x, w[i], label=f"{int(T[i])}K ({int(T[i]) - Temp_Kelvin}$^\circ C$)")
    plt.legend(title='Temperature', title_fontsize=9, fontsize=8)
    plt.grid(True)

    plt.figure(2)
    plt.xlabel('wavelength')
    plt.ylabel('power density')
    if i % 2 == 1:
        plt.plot(x, w[i], label=f"{int(T[i])}K ({int(T[i]) - Temp_Kelvin}$^\circ C$)", linestyle='--')
    else:
        plt.plot(x, w[i], label=f"{int(T[i])}K ({int(T[i]) - Temp_Kelvin}$^\circ C$)")
    plt.legend(title='Temperature', title_fontsize=9, fontsize=8)
    plt.grid(True)

    # plt.figure(3)
    # plt.yscale("log")
    # plt.xlabel('wavelength')
    # plt.ylabel('intensity(log)')
    # plt.plot(x, lw[i])


# w_max = np.max(w)
# max_lambda = x.index(max(x))

# w_max = np.where(w == np.max(w[i]))
# print(i)
# print(w_max)
# print('temperature ', T[i])
# print('peak wavelength of temperature %s = %s' % (T[i], x[np.argmax(w[i])]))

plt.show()

# ww : power density at specific wavelength w_t
# w_t : given wavelength wavelength_test
# temperature calculation from power density at given wavelength
# T_c = (h*c) / ((k*w_t)*np.log(((2*np.pi*h*c**2)/((ww*w_t**5))+1)))
