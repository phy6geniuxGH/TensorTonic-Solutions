import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    values = np.array(values, dtype = np.float64)
    w = (np.max(values) - np.min(values))/num_bins
    bins = []
    for i in values:
        bins.append(min(np.floor((i - min(values))/w),num_bins-1))
    print(bins)
    # Check if bins contain NaNs
    bins_check = np.isnan(bins)
    print(bins_check)
    if all(bins_check):
        return np.zeros(len(values)).tolist()
    else:
        return(bins)