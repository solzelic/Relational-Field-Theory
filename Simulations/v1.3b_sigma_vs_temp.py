import numpy as np
import matplotlib.pyplot as plt

# Constants
k_B = 1.0
tau_dec = 1.0
Gamma_th = 0.5
J = 0.2

# Temperature range
T_env_values = np.linspace(0.1, 2.0, 100)

# Sigma computation
sigma_values = k_B * T_env_values * tau_dec * np.sqrt(Gamma_th / J)

# Plot
plt.figure(figsize=(8,5))
plt.plot(T_env_values, sigma_values, color='blue', label=r'$\sigma(T) = k_B T \tau_{dec} \sqrt{\Gamma_{th} / J}$')
plt.xlabel('Environment Temperature ($T_{env}$)')
plt.ylabel('Collapse Sensitivity ($\sigma$)')
plt.title('RFT Simulation V1.3b: $\sigma$ vs Temperature')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('../Figures/figure_2_sigma_vs_temperature.png', dpi=300)
plt.show()