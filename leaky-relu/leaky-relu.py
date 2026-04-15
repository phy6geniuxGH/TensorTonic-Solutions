import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    output = []
    for i in x:
        output.append(i if i >= 0 else alpha*i)

    return np.array(output, dtype = np.float64)