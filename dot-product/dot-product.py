import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    a = np.asarray(x, dtype=float)
    b = np.asarray(y, dtype=float)

    return np.dot(a, b)