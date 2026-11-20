import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    X=np.asarray(x,dtype=float)
    P=np.asarray(p,dtype=float)

    discrete_value=np.dot(X,P)

    return discrete_value
    