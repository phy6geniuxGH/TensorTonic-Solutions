import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here    
    if (len(set(y_true))==1) & (y_true == y_pred):
        return 1.0
    elif (len(set(y_true))==1) & (y_true != y_pred):
        return 0.0
    else:
        y_true = np.array(y_true, dtype = np.float64)
        y_pred = np.array(y_pred, dtype = np.float64)
    
        r_squared = 1 - (np.sum((y_true - y_pred)**2))/(np.sum((y_true - np.mean(y_true))**2))
    
        print(r_squared)
        
        return r_squared
