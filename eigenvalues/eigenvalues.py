import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    A = np.array(matrix, dtype=float)
    eigenvalues = np.linalg.eigvals(A)
    return np.sort(np.real(eigenvalues))