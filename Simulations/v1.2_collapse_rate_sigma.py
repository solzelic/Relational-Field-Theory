import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit as sigmoid  # sigmoid for Γ(R)

# Constants
hbar = 1.0
k_B = 1.0
E_c = 1.0
Gamma_th = 0.5
d = 2
S_vN = 0.6
J = 0.2

# Compute collapse threshold θ
theta = (hbar / J) * (S_vN / d) * E_c

# Time setup
timesteps = 300
t_list = np.linspace(0, 20, timesteps)
dt = t_list[1] - t_list[0]

# Define relational field function R(t)
def R_t(t, J, S_vN):
    return J * (1 + np.sin(t)) * S_vN

# Compute ∫R(t) dt
R_integral = 0
R_integrals = []
for t in t_list:
    R_now = R_t(t, J, S_vN)
    R_integral += R_now * dt
    R_integrals.append(R_integral)

# σ values to compare: small (sharp), medium, large (soft)
sigma_values = [0.05, 0.5, 5.0]
colors = ['red', 'orange', 'green']
labels = ['Sharp Collapse (σ=0.05)', 'Medium (σ=0.5)', 'Soft (σ=5.0)']

# Plot setup
plt.figure(figsize=(10, 6))
plt.plot(t_list, R_integrals, label='∫R(t) dt', color='blue', linewidth=2)
plt.axhline(y=theta, color='black', linestyle='--', label='θ (collapse threshold)', linewidth=1)

# Plot Γ(R) for each σ
for idx, sigma in enumerate(sigma_values):
    gamma_curve = [sigmoid((r - theta) / sigma) for r in R_integrals]
    plt.plot(t_list, gamma_curve, label=labels[idx], color=colors[idx], linewidth=2)

# Labels and formatting
plt.title("RFT Simulation V1.2: Collapse Rate Γ(R) for Varying σ")
plt.xlabel("Time")
plt.ylabel("Collapse Rate Γ(R) and ∫R(t) dt")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()