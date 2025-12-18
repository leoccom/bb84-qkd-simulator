import numpy as np
from src.constants import ZERO, ONE, PLUS, MINUS


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