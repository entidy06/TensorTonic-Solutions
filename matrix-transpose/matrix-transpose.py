import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    a = np.asarray(A, dtype=float)
    (m, n) = np.shape(a)
    output = np.zeros((n, m))
    for i in range(m):
        for j in range(n):
            output[j][i] = a[i][j]
        
    return output
