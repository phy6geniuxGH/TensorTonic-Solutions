import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    v = np.asarray(v, dtype = np.float64)
    if v.ndim == 1:
        return np.linalg.norm(v)
    else:
        return np.array([np.linalg.norm(i) for i in v])