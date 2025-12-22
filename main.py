import numpy as np
from src.constants import BASIS_STANDARD, ZERO, ONE, PLUS, MINUS
from src.eve import Eve
from src.qubit import Qubit
from collections import Counter
from src.alice import Alice
from src.bob import Bob
from src.utils import sift_keys, calculate_qber


# Check Magnitude
length_plus = np.linalg.norm(PLUS)
print(f"Length of PLUS state: {length_plus}")
print(f"Is length 1? {np.isclose(length_plus, 1)}")

# Check Orthogonality (between ZERO and ONE)
dot_product = np.dot(ZERO, ONE)
print(f"Dot product of ZERO and ONE: {dot_product}")
print(f"Are they orthogonal? {np.isclose(dot_product, 0)}")

# Check superposition
overlap = np.dot(ZERO, PLUS)
print(f"Overlap of ZERO and PLUS: {overlap}")
print(f"Expected: {1/np.sqrt(2)}")


# Qubit Verification
# Test 1: Deterministic
q1_output = []
for _ in range(100):
    q1 = Qubit(ZERO)
    q1_output.append(q1.measure(BASIS_STANDARD))

# Test 2: Probabilistic
q2_output = []
for _ in range(10000):
    q2 = Qubit(PLUS)
    q2_output.append(q2.measure(BASIS_STANDARD))

print(f"q1 (Should be all 0s): {Counter(q1_output)}")
print(f"q2 (Should be ~50/50): {Counter(q2_output)}")



# Simulate Communication
n_qubits = 1000
alice = Alice(n_qubits)
bob = Bob(n_qubits)
eve = Eve(n_qubits)

# Alice sends Qubit list
alice._generate_random_bits()
alice._generate_random_bases()
traffic = alice.create_qubits() # List of Qubit Objects

# Eve intercepts Qubit list
eve._generate_random_bases()
new_traffic = eve.intercept_qubits(traffic) # New List of Qubit Objects

# Bob receives Qubit list
bob._generate_random_bases()
bob.measure_qubits(new_traffic)

# Alice and Bob compare their "Bases". (Not "Bits" since they will be used as a key)
# print(f"Bases of Alice: {alice.bases}")
# print(f"Bases of Bob: {bob.bases}")

alice_sift_key, bob_sift_key = sift_keys(alice.bases, bob.bases, alice.bits, bob.bits)

qber = calculate_qber(alice_sift_key, bob_sift_key)

print(f"Alice's sifted key: {alice_sift_key}, '\n', Bob's sifted key: {bob_sift_key}")
print(f"Are they same?: {np.all(alice_sift_key == bob_sift_key)}")
print(f"QBER value: {qber}")
# QBER Values: 0 - Perfect Channel, .25 - Eve Listening, .5 - Broken System