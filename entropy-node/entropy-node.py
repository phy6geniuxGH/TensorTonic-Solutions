import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if all(y):
        return 0.0
    else:
        
        unique_elements, counts = np.unique(np.array(y,dtype=np.float64), return_counts = True)
        p = counts/len(y)
        S = -sum((p)*np.log2((p)))
        return S