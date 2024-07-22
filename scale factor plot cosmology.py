import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Function for the differential equation
def syseq(y, t, Omega_m, Omega_r, Omega_l, Omega_k, H0):
    dydt = [y[1],
            (-(H0 ** 2 / 2) * (Omega_m / y[0] ** 3 + 2 * Omega_r / y[0] ** 4 - 2 * Omega_l)) * Omega_m * (
                        1 / (H0 ** 2) * y[1] ** 2 -
                        Omega_r / y[0] ** 2 - Omega_l * y[0] ** 2 - Omega_k) ** (-1)]
    return dydt

# Cosmological parameters
H0 = 67400 / (3.09 * 10 ** 22) * (3600 * 24 * 365 * 10 ** 9)
Omega = [
    {"M": 0.3, "R": 1e-4, "L": 0, "K": 1 - 0.3 - 1e-4 - 0},  # Model 1
    {"M": 0.3, "R": 1e-4, "L": 0.7, "K": 1 - 0.3 - 1e-4 - 0.7},  # Model 2
    {"M": 5, "R": 1e-4, "L": 0, "K": 1 - 5 - 1e-4 - 0},  # Model 3
]
t_limits = [[0, -15], [0, 30]]  # Initial and final time for each model

# Initial conditions
init_conditions = [[1, H0 * (model["M"] / 1 + model["R"] / (1 ** 2) + model["K"] + model["L"] * (1 ** 2)) ** (1 / 2)]
                   for model in Omega]

# Color palette for the curves
colors = ['b', 'r', 'g']

# Resolution for each model and plot
plt.figure(figsize=(14, 10))
for i, (limits, init, color) in enumerate(zip(t_limits, init_conditions, colors), start=1):
    t = np.linspace(limits[0], limits[1], 100000)
    for model, c in zip(Omega, colors):
        sol = odeint(syseq, init, t, args=(model["M"], model["R"], model["L"], model["K"], H0))
        plt.plot(t, sol[:, 0], linestyle='-', color=c)

# Adjust font sizes
plt.xlabel('Cosmic Time $t$ [Gyr]', fontsize=14)
plt.ylabel('Scale Factor $a(t)$ [/]', fontsize=14)
plt.ylim([0, 4])
plt.title('Scale Factor as a Function of Time', fontsize=16)
plt.legend([f'$\Omega_M={Omega[0]["M"]}, \Omega_R=10^{np.log10(Omega[0]["R"])}, \Omega_Λ={Omega[0]["L"]}$', 
            f'$\Omega_M={Omega[1]["M"]}, \Omega_R=10^{np.log10(Omega[1]["R"])}, \Omega_Λ={Omega[1]["L"]}$', 
            f'$\Omega_M={Omega[2]["M"]}, \Omega_R=10^{np.log10(Omega[2]["R"])}, \Omega_Λ={Omega[2]["L"]}$'], fontsize=14)
plt.grid(True)
plt.show()
