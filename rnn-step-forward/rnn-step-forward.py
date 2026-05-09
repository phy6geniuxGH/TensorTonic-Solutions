import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    x_t = np.array(x_t, dtype=np.float64)
    h_prev = np.array(h_prev, dtype=np.float64)
    Wx = np.array(Wx, dtype=np.float64)
    Wh = np.array(Wh, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    return np.tanh(x_t @ Wx + h_prev @ Wh + b)