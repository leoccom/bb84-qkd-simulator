# Run the full BB84 protocol multiple times with different parameters

# Run this file via `python3 -m src.experiment`

import numpy as np
import matplotlib.pyplot as plt
from src.alice import Alice
from src.bob import Bob
from src.eve import Eve
from src.utils import sift_keys, calculate_qber


x_values = []
y_values = []
n_qubits = 10000

# The Simulation Function
def run_single_experiment(eve_interception_rate: float) -> float:
    """
    Run the full BB84 protocol a single time with a given Eve interception rate.

    Parameters
    ----------
    eve_interception_rate : float
        The probability of Eve intercepting a Qubit.

    Returns
    -------
    qber : float
        The Quantum Bit Error Rate (QBER) of the experiment.
    """
    alice = Alice(n_qubits)
    bob = Bob(n_qubits)
    eve = Eve(n_qubits, rate)

    alice._generate_random_bases()
    alice._generate_random_bits()
    traffic = alice.create_qubits()

    eve._generate_random_bases()
    new_traffic = eve.intercept_qubits(traffic)

    bob._generate_random_bases()
    bob.measure_qubits(new_traffic)

    alice_sift_key, bob_sift_key = sift_keys(alice.bases, bob.bases, alice.bits, bob.bits)

    qber = calculate_qber(alice_sift_key, bob_sift_key)

    return qber


# Data Collection Loop
for rate in np.linspace(0.0, 1.0, num=21):
    x_values.append(rate)

    qber = run_single_experiment(rate)

    y_values.append(qber)


# Visualization
plt.plot(x_values, y_values, color='k', label="Measurement")
plt.xlabel("Interception Rate (Eve)")
plt.ylabel("Quantum Bit Error Rate (QBER)")
plt.hlines(0.25, 0.0, 1.0, color='r', label="Theoretical Max Error")
plt.title("Effect of Eavesdropping on Quantum Security")
plt.legend()
plt.show()

### QBER ∝ Interception Rate