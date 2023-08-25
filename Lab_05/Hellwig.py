import numpy as np
from scipy.stats import pearsonr

correlation_with_y = np.array([0.6, -0.9, 0.2])
correlation_matrix = np.matrix([[1, -0.3, 0.5],
                    [-0.3, 1, -0.1],
                    [0.5, -0.1, 1]])


def hellwig_method(correlation_matrix, correlation_with_y):
    num_vars = correlation_matrix.shape[0]
    selected_vars = []
    remaining_vars = list(range(num_vars))
    
    while remaining_vars:
        max_diff = -np.inf
        selected_var = None
        
        for var in remaining_vars:
            corr_with_y = correlation_with_y[var]
            # print(corr_with_y)
            # print(correlation_matrix[selected_vars + [var]][:, selected_vars + [var]])
            corr_sum = np.sum(correlation_matrix[selected_vars + [var]][:, selected_vars + [var]])
            diff = corr_with_y - corr_sum
            
            if diff > max_diff:
                max_diff = diff
                selected_var = var
        
        if selected_var is not None:
            selected_vars.append(selected_var)
            remaining_vars.remove(selected_var)
        else:
            break
    
    return selected_vars


selected_indices = hellwig_method(correlation_matrix, correlation_with_y)
print("Selected variables indices:", selected_indices)