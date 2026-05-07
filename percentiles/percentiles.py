import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.array(x, dtype = np.float64)
    output = []
    for p in q:
        output.append(np.percentile(x,p,method='linear'))
    output = np.array(output)
    return output
        