import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v, dtype = np.float64)
    print(v.ndim)
    if v.ndim == 1:
        norm = np.linalg.norm(v)
        unit_vec = v/norm
        return unit_vec if norm != 0 else v
    else:
        norm = np.linalg.norm(v, axis=1, keepdims=True)
        unit_vec = v/(norm+1e-10)
        return unit_vec