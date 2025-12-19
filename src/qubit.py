import numpy as np
from src.constants import ZERO, ONE, PLUS, MINUS, BASIS_STANDARD, BASIS_HADAMARD

class Qubit:
    def __init__(self, state_vector: np.array):
        self.state = state_vector
    
    def measure(self, basis: str) -> int:
        """
        Measure the qubit state in the given basis.
        
        Parameters
        ----------
        basis : str
            The basis to measure in. Either BASIS_STANDARD or BASIS_HADAMARD.
        
        Returns
        -------
        outcome_bit : int
            The outcome of the measurement. Either 0 or 1.
        """
        if basis == BASIS_STANDARD: # Basis Standard
            basis_0 = ZERO
            basis_1 = ONE
        elif basis == BASIS_HADAMARD: # Basis Hadamard
            basis_0 = PLUS
            basis_1 = MINUS
        else:
            raise ValueError("Invalid Basis")
        
        prob_0 = (np.dot(self.state, basis_0))**2 # Probability of getting 0 (|0> or |+>)
        outcome_bit = np.random.choice([0, 1], p=[prob_0, 1 - prob_0])

        if outcome_bit == 0:
            self.state = basis_0
        else: # outcome_bit == 1
            self.state = basis_1

        return outcome_bit