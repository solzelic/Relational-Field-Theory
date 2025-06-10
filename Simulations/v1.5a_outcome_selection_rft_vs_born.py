import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
hbar = 1.0
k_B = 1.0
E_c = 1.0
Gamma_th = 0.5
d = 2
S_vN = 0.6
J = 0.2
T_env = 0.5

# Collapse threshold and sensitivity
theta = (hbar / J) * (S_vN / d) * E_c
tau_dec = 1 / (J**2)
sigma = k_B * T_env * tau_dec * np.sqrt(Gamma_th / J)

# Define relational field functions for each outcome branch
def R_i(t, i):
    # You can change this to introduce bias if needed
    return J * (1 + np.sin(t + i)) * S_vN

# Time parameters
timesteps = 300
t_list = np.linspace(0, 20, timesteps)
dt = t_list[1] - t_list[0]

# Run 100 outcome selection trials
num_trials = 100
results_rft = []

for trial in range(num_trials):
    R0_integral, R1_integral = 0, 0
    collapsed = False

    for t in t_list:
        R0_integral += R_i(t, 0) * dt
        R1_integral += R_i(t, 1) * dt
        if not collapsed and (R0_integral + R1_integral) >= theta:
            # Use RFT-weighted Born rule for outcome selection
            amp_0 = 1 / np.sqrt(2)
            amp_1 = 1 / np.sqrt(2)
            weight_0 = (abs(amp_0)**2) * R0_integral
            weight_1 = (abs(amp_1)**2) * R1_integral
            total = weight_0 + weight_1
            p0 = weight_0 / total
            outcome = np.random.choice(["0", "1"], p=[p0, 1 - p0])
            results_rft.append(outcome)
            collapsed = True
            break

# Count outcomes
count_0 = results_rft.count("0")
count_1 = results_rft.count("1")

# Plot results
plt.figure(figsize=(8, 5))
plt.bar(["|0⟩", "|1⟩"], [count_0, count_1], color=["skyblue", "salmon"])
plt.title("RFT Simulation V1.5a: Outcome Selection Over 100 Trials")
plt.ylabel("Collapse Frequency")
plt.grid(axis='y')
plt.tight_layout()
plt.show()