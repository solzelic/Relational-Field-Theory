import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit as sigmoid

# Constants
hbar = 1.0
k_B = 1.0
E_c = 1.0
Gamma_th = 0.5
d = 2
S_vN = 0.6
J = 0.2
theta = (hbar / J) * (S_vN / d) * E_c
tau_dec = 1 / (J**2)

# Time setup
timesteps = 300
t_list = np.linspace(0, 20, timesteps)
dt = t_list[1] - t_list[0]

# Accumulate R(t)
R_integrals = []
R_accum = 0
for t in t_list:
    R_now = J * (1 + np.sin(t)) * S_vN
    R_accum += R_now * dt
    R_integrals.append(R_accum)

# σ values to test
sigma_values = [0.05, 0.5, 5.0]
colors = ['red', 'orange', 'green']

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t_list, R_integrals, label="∫R(t) dt", color='blue')

for idx, sigma in enumerate(sigma_values):
    gamma_t = [sigmoid((r - theta) / sigma) for r in R_integrals]

    # Detect collapse time (when Γ crosses 0.5)
    collapse_time = None
    for i, g in enumerate(gamma_t):
        if g >= 0.5:
            collapse_time = t_list[i]
            break

    plt.plot(t_list, gamma_t, color=colors[idx], label=f"Γ(R) – σ = {sigma}")
    if collapse_time:
        plt.axvline(collapse_time, color=colors[idx], linestyle='--', alpha=0.5)

# Threshold line
plt.axhline(theta, color='black', linestyle='--', linewidth=1.2, alpha=0.6, label='θ (threshold)')

plt.title("RFT Simulation V1.5b: Collapse Timing vs Sensitivity σ")
plt.xlabel("Time")
plt.ylabel("Γ(R) and ∫R(t) dt")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()