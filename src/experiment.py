# Run the full BB84 protocol multiple times with different parameters

import numpy as np
import matplotlib.pyplot as plt
from src.alice import Alice
from src.bob import Bob
from src.eve import Eve
from src.utils import sift_keys, calculate_qber


x_values = []
y_values = []
n_qubits = 5000



for rate in np.linspace(0.0, 1.0, num=11):
    x_values.append(rate)
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

    y_values.append(qber)


plt.plot(x_values, y_values, color='r', label="Measurement")
plt.xlabel("Interception Rate (Eve)")
plt.ylabel("Quantum Bit Error Rate (QBER)")
plt.plot([0, 1], [0, 0.25], color='b', alpha=0.5, label="Expected Line")
plt.title("Effect of Eavesdropping on Quantum Security")
plt.legend()
plt.show()

### QBER ∝ Interception Rate