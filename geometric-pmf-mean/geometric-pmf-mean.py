import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k = np.array(k, dtype = np.float64)
    pmf = p*(1 - p)**(k-1)
    mean = 1/p
    return (pmf, mean)