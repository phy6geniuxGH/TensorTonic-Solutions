import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.array(x, dtype=np.float64)
    return x*(1/(1+np.exp(-x)))