from matrices import compute_all_binary_matrices 
from variance import compute_variance

def compute_variances(m, n):
    variances = []
    binary_matrices = compute_all_binary_matrices(m, n)
    for matrix in binary_matrices:
        model_variace = compute_variance(matrix)
        if model_variace == 0:
            print('JE TAM NULA !')
        variances.append(round(model_variace, 3))
    return variances

variances = compute_variances(3, 4)
minimum = min(variances)

print(len(variances))
print(minimum)