import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x, dtype = np.float64)
    dct = Counter(x)
    print(dct)
    mode = max(dct, key=dct.get)
    return (
        np.mean(x),
        np.median(x),
        mode
    )