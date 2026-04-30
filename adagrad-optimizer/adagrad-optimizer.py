import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    G = np.array(G, dtype=np.float64)
    w = np.array(w, dtype=np.float64)

    newG = []
    new_w = []
    for i in range(len(w)):
        ng = G[i]+ g[i]**2
        newG.append(ng)
        new_w.append(w[i] - (lr/(np.sqrt(ng + eps)))*g[i])

    return (newG, new_w)[::-1]