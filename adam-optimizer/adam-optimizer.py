import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    param = np.array(param, dtype=np.float64)
    grad = np.array(grad, dtype=np.float64)
    m = np.array(m, dtype=np.float64)
    v = np.array(v, dtype=np.float64)
    
    # 2. Update biased first and second moment estimates
    m_new = beta1 * m + (1.0 - beta1) * grad
    v_new = beta2 * v + (1.0 - beta2) * (grad**2)
    
    # 3. Compute bias-corrected estimates (The "heck is this" part)
    # These compensate for m and v starting at 0
    m_hat = m_new / (1.0 - beta1**t)
    v_hat = v_new / (1.0 - beta2**t)
    
    # 4. Update parameters
    # CRITICAL: To get 0.000999, move eps OUTSIDE the sqrt
    new_param = param - lr * m_hat / (np.sqrt(v_hat) + eps)
    
    return new_param, m_new, v_new
    