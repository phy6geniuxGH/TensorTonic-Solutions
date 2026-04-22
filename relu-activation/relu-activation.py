import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x = np.array(x, dtype = np.float64)
    relu_x = np.maximum(0,x)
    return relu_x