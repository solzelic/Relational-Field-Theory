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

# Collapse threshold and sensitivity
theta = (hbar / J) * (S_vN / d) * E_c
tau_dec = 1 / (J**2)
sigma = k_B * T_env * tau_dec * np.sqrt(Gamma_th / J)

# Time setup
timesteps = 300
t_list = np.linspace(0, 20, timesteps)
dt = t_list[1] - t_list[0]

# Relational field accumulation
R_integral = 0
R_integrals = []
for t in t_list:
    R_now = J * (1 + np.sin(t)) * S_vN
    R_integral += R_now * dt
    R_integrals.append(R_integral)

# Collapse rate function
gamma_t = [sigmoid((r - theta) / sigma) for r in R_integrals]

# Initial states
psi1 = basis(2, 1)                         # Test A: start in excited state
psiB = (basis(2, 0) + basis(2, 1)).unit()  # Test B: equal superposition

# Collapse operator: decay toward |0⟩
c_op = sigmam()

# Time-dependent collapse function
def gamma_func(t, args):
    idx = int(t / dt)
    return gamma_t[idx] if idx < len(gamma_t) else 0

c_ops = [[c_op, gamma_func]]

# Test A – collapse into |0⟩
rho1 = ket2dm(psi1)
res_A = mesolve(0.5 * sigmaz(), rho1, t_list, c_ops, [num(2)])  # tracks ⟨1|ρ(t)|1⟩

# Test B – superposition and coherence loss
rhoB = ket2dm(psiB)
coherence_op = Qobj([[0, 1], [0, 0]])  # extract ρ_01
res_B = mesolve(0.5 * sigmaz(), rhoB, t_list, c_ops, [num(2), coherence_op])

# Plot results
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

# Test A
ax[0].plot(t_list, res_A.expect[0], color='red', label="⟨1|ρ(t)|1⟩ – Test A")
ax[0].set_title("Test A – Collapse into |0⟩ from Excited State")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Population in |1⟩")
ax[0].legend()
ax[0].grid(True)

# Test B
ax[1].plot(t_list, res_B.expect[0], label="⟨1|ρ(t)|1⟩ – Population")
ax[1].plot(t_list, [abs(c) for c in res_B.expect[1]], label="|ρ₀₁(t)| – Coherence")
ax[1].set_title("Test B – Superposition Collapse and Coherence Loss")
ax[1].set_xlabel("Time")
ax[1].set_ylabel("Value")
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.show() 