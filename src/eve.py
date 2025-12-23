# Receiver & Sender

import numpy as np
from src.qubit import Qubit
from src.constants import ZERO, ONE, PLUS, MINUS, BASIS_STANDARD, BASIS_HADAMARD


class Eve:
    def __init__(self, n_qubits: int, rate: float):
        self.n_qubits = n_qubits # The number of qubits she expects to catch
        self.bases = [] # Her random list of basis "guesses"
        self.interception_rate = rate
    
    def _generate_random_bases(self):
        for _ in range(self.n_qubits):
            self.bases.append(np.random.choice([BASIS_STANDARD, BASIS_HADAMARD]))
    
    def intercept_qubits(self, qubit_list: list[Qubit]) -> list[Qubit]:
        new_qubit_list = []
        for (qubit, basis) in zip(qubit_list, self.bases):
            num = np.random.rand()
            
            if num <= self.interception_rate: # Measure Qubit
                measured_bit = qubit.measure(basis)

                if basis == BASIS_STANDARD:
                    if measured_bit == 0:
                        new_qubit_list.append(Qubit(ZERO))
                    else:
                        new_qubit_list.append(Qubit(ONE))
                elif basis == BASIS_HADAMARD:
                    if measured_bit == 0:
                        new_qubit_list.append(Qubit(PLUS))
                    else:
                        new_qubit_list.append(Qubit(MINUS))
                else:
                    raise ValueError("Wrong Basis")
            
            else: # Pass Original Qubit Untouched
                new_qubit_list.append(qubit)
        
        return new_qubit_list