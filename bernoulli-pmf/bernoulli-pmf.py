import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    X = np.asarray(x)

    # Calculate PMF: p when x == 1, and (1 - p) when x == 0
    pmf = np.where(X == 1, float(p), 1.0 - float(p))

    # Calculate moments as standard Python floats
    mean = float(p)
    variance = float(p * (1.0 - p))

    return {"pmf": pmf, "mean": mean, "variance": variance}