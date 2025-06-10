import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit as sigmoid
from qutip import *

# Constants
hbar = 1.0
k_B = 1.0
E_c = 1.0
Gamma_th = 0.5
d = 2
S_vN = 0.6
J = 0.2
T_env = 0.5

# Calculate RFT collapse parameters
theta = (hbar / J) * (S_vN / d) * E_c
tau_dec = 1 / (J**2)
sigma = k_B * T_env * tau_dec * np.sqrt(Gamma_th / J)

# Time setup
timesteps = 300
t_list = np.linspace(0, 20, timesteps)
dt = t_list[1] - t_list[0]

# Accumulate R(t)
R_integral = 0
R_integrals = []
for t in t_list:
    R_now = J * (1 + np.sin(t)) * S_vN
    R_integral += R_now * dt
    R_integrals.append(R_integral)

# Collapse rate function Γ(R)
gamma_t = [sigmoid((r - theta) / sigma) for r in R_integrals]

# Define system: Qubit and initial state
H = 0.5 * sigmaz()         # Hamiltonian
psi0 = basis(2, 0)         # Start in ground state |0>
rho0 = ket2dm(psi0)        # Density matrix

# Collapse operator (collapse to |0>)
c_op = sigmam()

# Time-dependent collapse rate
def gamma_func(t, args):
    idx = int(t / dt)
    return gamma_t[idx] if idx < len(gamma_t) else 0

# List of collapse operators with time-dependent rate
c_ops = [[c_op, gamma_func]]

# Solve master equation
result = mesolve(H, rho0, t_list, c_ops, [num(2)])  # ⟨1|ρ(t)|1⟩

# Plot result
plt.figure(figsize=(10, 6))
plt.plot(t_list, result.expect[0], label="⟨1|ρ(t)|1⟩ (Excited State Population)", color='purple')
plt.title("RFT Simulation V1.4: Density Matrix Evolution with Collapse")
plt.xlabel("Time")
plt.ylabel("Population in |1⟩")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()