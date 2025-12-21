import numpy as np


def sift_keys(bases_a: np.array, bases_b: np.array, bits_a: np.array , bits_b: np.array):
    """
    Shift the bits of two arrays based on the matching of their corresponding basis arrays.

    Parameters
    ----------
    bases_a : np.array
        The first basis array.
    bases_b : np.array
        The second basis array.
    bits_a : np.array
        The first bit array.
    bits_b : np.array
        The second bit array.

    Returns
    -------
    sift_key_a : np.array
        The first sifted key.
    sift_key_b : np.array
        The second sifted key.
    """
    sift_key_a = []
    sift_key_b = []

    for (i, (basis_a, basis_b)) in enumerate(zip(bases_a, bases_b)):
        if basis_a == basis_b:
            sift_key_a.append(bits_a[i])
            sift_key_b.append(bits_b[i])
    
    sift_key_a = np.array(sift_key_a)
    sift_key_b = np.array(sift_key_b)
    return (sift_key_a, sift_key_b)


def calculate_qber(sift_key_a, sift_key_b) -> float:
    """
    Calculate the Quantum Bit Error Rate (QBER) from two sifted keys.

    Parameters
    ----------
    sift_key_a : np.array
        The first sifted key.
    sift_key_b : np.array
        The second sifted key.

    Returns
    -------
    qber : float
        The Quantum Bit Error Rate (QBER). A value between 0 and 1.
        0:     Perfect Channel (No Eavesdropper)
        ~.25:  Someone (Eve) is intercepting
        .50:   Broken System
    """
    error_count = 0
    key_length = len(sift_key_a)

    for (i, (bit_a, bit_b)) in enumerate(zip(sift_key_a, sift_key_b)):
        if bit_a != bit_b:
            error_count += 1
    
    qber = (error_count / key_length)
    return qber