# Sender
import numpy as np
from src.qubit import Qubit
from src.constants import ZERO, ONE, PLUS, MINUS, BASIS_STANDARD, BASIS_HADAMARD

class Alice:
    def __init__(self, n_qubits):
        self.n_qubits = n_qubits # How many bits she wants to send
        self.bits = [] # A list of random integers (0s and 1s)
        self.bases = [] # A list of random choices (BASIS_STANDARD or BASIS_HADAMARD)
    
    def _generate_random_bits(self):
        for _ in range(self.n_qubits):
            self.bits.append(np.random.choice([0, 1]))
    
    def _generate_random_bases(self):
        for _ in range(self.n_qubits):
            self.bases.append(np.random.choice([BASIS_STANDARD, BASIS_HADAMARD]))
    
    def create_qubits(self) -> list[Qubit]:
        qubits = []
        for (bit, basis) in zip(self.bits, self.bases):
            if basis == BASIS_STANDARD:
                if bit == 0:
                    qubits.append(Qubit(ZERO))
                elif bit == 1:
                    qubits.append(Qubit(ONE))
                else:
                    raise ValueError("Wrong bit")
            elif basis == BASIS_HADAMARD:
                if bit == 0:
                    qubits.append(Qubit(PLUS))
                elif bit == 1:
                    qubits.append(Qubit(MINUS))
                else:
                    raise ValueError("Wrong bit")
            else:
                raise ValueError("Wrong basis")
        
        return qubits
