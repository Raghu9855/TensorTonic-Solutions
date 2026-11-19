from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    sorted_x = sorted(x)
    n = len(sorted_x)
    
    # 1. Mean
    mean = sum(sorted_x) / n
    
    # 2. Median
    mid = n // 2
    if n % 2 == 1:
        median = sorted_x[mid]
    else:
        median = (sorted_x[mid - 1] + sorted_x[mid]) / 2
        
    # 3. Mode (picks the smallest mode if there is a tie)
    counts = Counter(sorted_x)
    max_freq = max(counts.values())
    modes = [num for num, freq in counts.items() if freq == max_freq]
    mode = modes[0]

    return {
        "mean": float(mean),
        "median": float(median),
        "mode": float(mode)
    }