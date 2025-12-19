import numpy as np
from src.constants import BASIS_STANDARD, ZERO, ONE, PLUS, MINUS
from src.qubit import Qubit
from collections import Counter


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