from project_math.matrices import compute_all_binary_matrices 
from project_math.variance import compute_variance

from helpers.minimum_with_indices import min_with_indices
from helpers.save_designs import save_designs

def compute_variances(m, n):
    variances = []
    binary_matrices = compute_all_binary_matrices(m, n)
    for matrix in binary_matrices:
        model_variace = compute_variance(matrix)
        variances.append(round(model_variace, 5))
    return binary_matrices, variances

def compute_optimal_designs(m, n):
    matrices, variances = compute_variances(m, n)
    indices = min_with_indices(variances)
    optimal_designs = []
    for i in indices:
        optimal_designs.append(matrices[i])
    return optimal_designs

optimal_designs = compute_optimal_designs(3, 7)
save_designs('data/optimal_designs', optimal_designs)

print('END')