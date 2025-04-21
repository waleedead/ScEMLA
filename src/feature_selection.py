import numpy as np

def run_genetic_algorithm(X, y=None, generations=50, pop_size=30):
    # Placeholder: random feature selection
    np.random.seed(42)
    selected = np.random.choice(X.columns, size=50, replace=False)
    return selected
