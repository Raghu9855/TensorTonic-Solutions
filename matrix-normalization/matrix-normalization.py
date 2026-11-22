import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    arr = np.asarray(matrix, dtype=np.float64)

    # 1. Compute the norm along the specified axis while keeping dimensions
    if norm_type == "l1":
        norms = np.sum(np.abs(arr), axis=axis, keepdims=True)
    elif norm_type == "l2":
        norms = np.sqrt(np.sum(arr**2, axis=axis, keepdims=True))
    elif norm_type == "max":
        norms = np.max(np.abs(arr), axis=axis, keepdims=True)
    else:
        raise ValueError(
            f"Unsupported norm_type: '{norm_type}'. Choose 'l1', 'l2', or 'max'."
        )

    # 2. Prevent division by zero: replace 0 norms with 1.0 so zero slices stay 0
    safe_norms = np.where(norms == 0, 1.0, norms)

    # 3. Divide and return
    return arr / safe_norms