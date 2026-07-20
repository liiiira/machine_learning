def generate_synthetic_linear_data(beta, low, high, size=None, noise=False, scale=1):
    
    if type(beta) != tuple:
        raise ValueError("beta paramter must be a tuple of length >= 2")
        
    beta = np.array(beta)
    
    rng = np.random.default_rng()
    
    X = rng.uniform(low=-3, high=3, size=(size, len(beta) - 1))
    X = np.insert(X, 0, 1, axis=1)
    
    y = X @ beta

    X = X[: , 1:]
    if noise:
        epsilons = rng.normal(loc=0, scale=scale, size=size)
        y += epsilons
        
    return (X, y)