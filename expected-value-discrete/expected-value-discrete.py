import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if np.sum(p)!=1.0:
        raise ValueError("p not sum to 1")

    # Write code here
    x = np.array(x)
    p = np.array(p)
    return np.dot(x,p) if np.sum(p)==1.0 else "ValueError"
