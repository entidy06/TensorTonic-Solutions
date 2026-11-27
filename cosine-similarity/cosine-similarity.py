import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    x = np.asarray(a, dtype=float)
    y = np.asarray(b, dtype=float)

    dot_res = np.dot(x, y)
    x_norm = np.linalg.norm(x) if np.linalg.norm(x) != 0 else 0.0
    y_norm = np.linalg.norm(y) if np.linalg.norm(y) != 0 else 0.0

    return float(dot_res / (x_norm * y_norm)) if (x_norm * y_norm != 0) else 0.0
    