import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    arr = np.asarray(x, dtype=float)
    n = arr.size
    mean = np.mean(arr)
    
    # Sample standard deviation with Bessel's correction (ddof=1)
    s = np.std(arr, ddof=1)
    
    # Handle zero sample variance edge case
    if s == 0.0:
        if mean == mu0:
            return 0
        return float(np.inf if mean > mu0 else -np.inf)
    
    se = s / np.sqrt(n)
    t_stat = (mean - mu0) / se
    
    return float(t_stat)