from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    a = np.asarray(x, dtype=float)
    mean = np.mean(a)
    med = np.median(a)
    values, counts = np.unique(a, return_counts=True)
    mode = values[np.argmax(counts)]

    return {"mean": mean, "median": med, "mode": mode}
    