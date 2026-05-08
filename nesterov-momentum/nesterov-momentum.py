import numpy as np

def nesterov_momentum_step(w, v, grad, lr=0.01, momentum=0.9):
    """
    Perform one Nesterov Momentum update step.
    """
    # Write code here
    w = np.array(w, dtype=np.float64) 
    v = np.array(v, dtype=np.float64) 
    grad = np.array(grad, dtype=np.float64)
    wl = w - float(momentum)*v
    new_v = float(momentum)*v + float(lr)*grad
    new_w = w - new_v
    print(new_w, new_v)
    return (new_w, new_v)