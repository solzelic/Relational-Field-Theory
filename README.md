# Relational Field Theory (RFT)
A thermodynamically grounded collapse model for quantum-to-classical transition.

This repository contains the complete simulation suite supporting the V3.4.1 manuscript of **Relational Field Theory (RFT)**, which proposes a deterministic, interaction-based alternative to spontaneous collapse and decoherence models.

---

## 🔬 Summary

Relational Field Theory defines collapse as the result of accumulated interaction between a quantum system and its environment, modeled by a time-integrated **relational field** \( R(t) \). Collapse occurs when this integrated interaction crosses a thermodynamic threshold \( \theta \), with sharpness modulated by a sensitivity parameter \( \sigma \), and rate governed by \( \Gamma(R) \), a sigmoid function.

---

## 🧪 Simulation Suite

| Version | File | Description |
|--------|-------|-------------|
| V1.3a | `v1.3a_theta_entropy_dimension.py` | Plots how \( \theta \) scales with entropy and Hilbert space dimension |
| V1.3b | `v1.3b_sigma_vs_temp.py` | Shows how collapse sensitivity \( \sigma \) increases linearly with temperature |
| V1.2  | `v1.2_collapse_rate_sigma.py` | Illustrates how \( \Gamma(R) \) behaves under different \( \sigma \) values |
| V1.5b | `v1.5b_collapse_timing_vs_sigma.py` | Demonstrates collapse timing sensitivity under varying \( \sigma \) |
| V1.4  | `v1.4_density_matrix_evolution.py` | Shows suppression of coherence as collapse activates |
| V1.4b | `v1.4b_operator_switch_and_superposition.py` | Simulates outcome selection under operator and superposition collapse |
| V1.5a | `v1.5a_outcome_selection_rft_vs_born.py` | Compares Born rule vs RFT-weighted projection under symmetric initial state |

---

## 📁 Folder Structure
Relational-Field-Theory/
├── README.md
├── LICENSE
├── docs/                     # Additional papers, references
├── figures/                  # Charts from simulations
├── simulations/              # Python scripts for each version
└── requirements.txt          # Python dependencies

---

## 🧰 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Relational-Field-Theory.git
   cd Relational-Field-Theory
2.	Create and activate a virtual environment:
  python3 -m venv rft_env
  source rft_env/bin/activate  # On Windows use: rft_env\Scripts\activate
3.	Install dependencies:
   pip install -r requirements.txt
5.	Run a simulation:
   python simulations/v1.3a_theta_entropy_dimension.py


📜 License

This project is licensed under the MIT License. See LICENSE for details.

⸻

🧠 Contributors

Sol Zelic
With support from GPT-4o and Claude-3-Opus
Relational Field Theory is an ongoing open-science collaboration.

