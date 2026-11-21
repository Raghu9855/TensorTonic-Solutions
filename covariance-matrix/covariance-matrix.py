import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    x=np.asarray(X)
    center_fea=x - np.mean(X, axis=0)
    return (center_fea.T @ center_fea) / (x.shape[0] - 1)