# Receiver

import numpy as np
from src.qubit import Qubit
from src.constants import ZERO, ONE, PLUS, MINUS, BASIS_STANDARD, BASIS_HADAMARD

class Bob:
    def __init__(self, n_qubits):
        self.n_qubits = n_qubits # # How many bits to receive
        self.bases = [] # A list of random choices (BASIS_STANDARD or BASIS_HADAMARD)
        self.bits = [] # The results of his measurements
    
    def _generate_random_bases(self):
        for _ in range(self.n_qubits):
            self.bases.append(np.random.choice([BASIS_STANDARD, BASIS_HADAMARD]))
    
    def measure_qubits(self, qubit_list: list[Qubit]):
        for (qubit, basis) in zip(qubit_list, self.bases):
            self.bits.append(qubit.measure(basis))