import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    y_true = np.array(y_true, dtype=np.float64)
    y_score = np.array(y_score, dtype=np.float64)

    
    li = np.maximum(np.zeros(len(y_true)), margin - y_true*y_score)
    return np.mean(li) if reduction=="mean" else np.sum(li)