import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    x=np.asarray(a)
    y=np.asarray(b)
    vec=np.dot(x,y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    if norm_x==0 or norm_y==0:
        return 0.0
    return float(vec/(norm_x*norm_y))
