import numpy as np
from src.constants import BASIS_STANDARD, ZERO, ONE, PLUS, MINUS
from src.qubit import Qubit
from collections import Counter
from src.alice import Alice
from src.bob import Bob


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
q1 = Qubit(ZERO)

# Test 1: Deterministic
q1_output = []
for _ in range(100):
    q1_output.append(q1.measure(BASIS_STANDARD))

# Test 2: Probabilistic
q2_output = []
for _ in range(10000):
    q2 = Qubit(PLUS)
    q2_output.append(q2.measure(BASIS_STANDARD))

print(f"q1 (Should be all 0s): {Counter(q1_output)}")
print(f"q2 (Should be ~50/50): {Counter(q2_output)}")



# Simulate Communication
alice = Alice(100)
bob = Bob(100)
matching_bases = []

alice._generate_random_bits()
alice._generate_random_bases()
traffic = alice.create_qubits() # List of Qubit objects

bob._generate_random_bases()
bob.measure_qubits(traffic)

# Alice and Bob compare their "Bases". (Not "Bits" since they will be used as a key)
print(f"Bases of Alice: {alice.bases}")
print(f"Bases of Bob: {bob.bases}")

for i, (basis_a, basis_b) in enumerate(zip(alice.bases, bob.bases)):
    if basis_a == basis_b:
        matching_bases.append(i)

print(f"Index of matching bases: {matching_bases}")

# Bits of Alice and Bob
print(f"Bits of Alice: {alice.bits}")
print(f"Bits of Bob: {bob.bits}")

# Alice and Bob generate key by collecting the bits where bases match
alice_key = [alice.bits[i] for i in matching_bases]
bob_key = [bob.bits[i] for i in matching_bases]

print(f"Length of keys of Alice and Bob: {len(alice_key), len(bob_key)} respectively.")
print(f"Alice key: {alice_key}, Bob key: {bob_key}")
print(f"Do they match?: {alice_key == bob_key}")