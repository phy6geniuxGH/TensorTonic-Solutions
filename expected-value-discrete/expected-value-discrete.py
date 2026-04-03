import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if (np.sum(p) != 1):
        raise ValueError("Sum of probability cannot be greater than 1")
    else:
        return np.sum(np.array(x)*np.array(p))
     
