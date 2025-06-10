import numpy as np
import matplotlib.pyplot as plt
# Constants
hbar = 1.0
E_c = 1.0
J = 0.2  # fixed coupling for this test

# Define entropy (S_vN) and dimension (d) ranges
entropy_values = np.linspace(0.1, 1.0, 10)  # from low to high entropy
dimension_values = [2, 4, 8, 16]  # discrete Hilbert space dimensions

# Prepare the plot
plt.figure(figsize=(10, 6))

# Plot θ for each dimension vs entropy
for d in dimension_values:
    theta_values = [(hbar / J) * (S / d) * E_c for S in entropy_values]
    plt.plot(entropy_values, theta_values, label=f'd={d}')

# Plot styling
plt.title("RFT Simulation V1.3a: Collapse Threshold θ vs Entropy for Varying Dimensions")
plt.xlabel("Entropy (S_vN)")
plt.ylabel("Collapse Threshold (θ)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()