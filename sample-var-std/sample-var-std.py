import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x, dtype=np.float64)
    var = np.std(x, ddof=1)**2
    std = np.std(x, ddof=1)
    return (var, std)