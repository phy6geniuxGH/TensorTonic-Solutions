import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    dot_prod = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)) 
    return 0 if np.isnan(dot_prod) else dot_prod
