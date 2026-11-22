import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    arr = np.asarray(X, dtype=np.float64)
    n_samples = arr.shape[0]

    # 1. Center the features by subtracting their column means
    centered = arr - np.mean(arr, axis=0, keepdims=True)

    # 2. Compute the sample covariance matrix Sigma (ddof=1)
    # Using (X_centered.T @ X_centered) / (N - 1)
    cov_matrix = (centered.T @ centered) / (n_samples - 1)

    # 3. Extract feature standard deviations from the diagonal of Sigma
    std_devs = np.sqrt(np.diag(cov_matrix))

    # 4. Compute the denominator matrix (sigma_i * sigma_j)
    denom = np.outer(std_devs, std_devs)

    # 5. Divide covariance by outer product of std_devs
    # Zero variance produces 0/0 -> NaN (matching the requirement)
    with np.errstate(divide="ignore", invalid="ignore"):
        corr_matrix = cov_matrix / denom

    return corr_matrix