import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    pmf = np.array([p if i == 1 else 1-p for i in x], dtype=np.float64)
    mu = p
    sig = p*(1-p)
    return (pmf, mu, sig) 