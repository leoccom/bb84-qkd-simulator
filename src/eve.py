# Receiver & Sender

import numpy as np
from src.qubit import Qubit
from src.constants import ZERO, ONE, PLUS, MINUS, BASIS_STANDARD, BASIS_HADAMARD


class Eve:
    def __init__(self, n_qubits: int):
        self.n_qubits = n_qubits # The number of qubits she expects to catch
        self.bases = [] # Her random list of basis "guesses"
    
    def _generate_random_bases(self):
        for _ in range(self.n_qubits):
            self.bases.append(np.random.choice([BASIS_STANDARD, BASIS_HADAMARD]))
    
    def intercept_qubits(self, qubit_list: list[Qubit]) -> list[Qubit]:
        new_qubit_list = []
        for (qubit, basis) in zip(qubit_list, self.bases):
            if basis == BASIS_STANDARD:
                if qubit.measure(basis) == 0:
                    new_qubit_list.append(Qubit(ZERO))
                elif qubit.measure(basis) == 1:
                    new_qubit_list.append(Qubit(ONE))
                else:
                    raise ValueError("Measurement Error")
            elif basis == BASIS_HADAMARD:
                if qubit.measure(basis) == 0:
                    new_qubit_list.append(Qubit(PLUS))
                elif qubit.measure(basis) == 1:
                    new_qubit_list.append(Qubit(MINUS))
                else:
                    raise ValueError("Measurement Error")
            else:
                raise ValueError("Wrong Basis")
        
        return new_qubit_list