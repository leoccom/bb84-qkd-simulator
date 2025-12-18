import numpy as np

# State Vectors

# |0> : Vertical Polarization
ZERO = np.array([1, 0])

# |1> : Horizontal Polarization
ONE = np.array([0, 1])

# |+> : 45 degree Polarization
PLUS = np.array([1/np.sqrt(2), 1/np.sqrt(2)]) 

# |-> : -45 degree Polarization
MINUS = np.array([1/np.sqrt(2), -1/np.sqrt(2)])


# Basis Definitions

BASIS_STANDARD = "STD"
BASIS_HADAMARD = "HAD"