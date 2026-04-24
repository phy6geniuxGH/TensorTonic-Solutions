import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here

    y_true = np.array(y_true, dtype = np.float64)
    y_pred = np.array(y_pred, dtype = np.float64)
    print(y_true)
    print(y_pred)
    
    e = y_true - y_pred
    abs_e = np.abs(e)
    print(e)

    output = []
    for i in range(len(y_true)):
        if abs_e[i] <= delta:
            print(f"1:{0.5*e**2}")
            output.append(float(0.5*e[i]**2))
        else:
            print(f"2:{delta*(abs_e[i] - 0.5*delta)}")
            output.append(float(delta*(abs_e[i] - 0.5*delta)))
            
    print(output)
    print(np.mean(output))
    return np.mean(output)