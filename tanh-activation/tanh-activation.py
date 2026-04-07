import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x, dtype = np.float64)
    tanh_value = (np.e**x - np.e**(-x))/(np.e**x + np.e**(-x))
    return tanh_value