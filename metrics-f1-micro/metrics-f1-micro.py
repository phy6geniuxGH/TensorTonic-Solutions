import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true = np.array(y_true, dtype = np.float64)
    y_pred = np.array(y_pred, dtype = np.float64)

    comparison = y_true == y_pred
    TP = sum(comparison)
    FP = len(y_true) - TP
    FN = len(y_pred) - TP

    f1m = (2 * TP)/(2 * TP + FP + FN)
    print(f1m)
    return f1m