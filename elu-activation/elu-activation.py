import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    x = np.array(x,dtype=np.float64)
    zeros = np.zeros(len(x))
    for i in range(len(zeros)):
        if x[i] > 0:
            zeros[i] = x[i]
        else:
            zeros[i] = alpha*(np.e**x[i] - 1)
    return zeros.tolist()