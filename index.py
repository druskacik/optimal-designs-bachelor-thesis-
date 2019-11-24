from matrices import compute_all_binary_matrices 
from variance import compute_variance

from helpers import min_with_indices

def compute_variances(m, n):
    variances = []
    binary_matrices = compute_all_binary_matrices(m, n)
    for matrix in binary_matrices:
        model_variace = compute_variance(matrix)
        variances.append(round(model_variace, 3))
    return binary_matrices, variances

def compute_optimal_designs(m, n):
    matrices, variances = compute_variances(m, n)
    indices = min_with_indices(variances)
    optimal_designs = []
    for i in indices:
        optimal_designs.append(matrices[i])
    return optimal_designs

def save_optimal_designs(designs):
    m, n = 0, 0
    if len(designs) > 0:
        m, n = designs[0].shape
    else:
        return
    text_file = open('optimal_designs/designs' + str(m) + 'x' + str(n) + '.txt', 'w')
    for index, design in enumerate(designs):
        text_file.write('Design ' + str(index + 1) + '\n')
        for row in design:
            text_row = ''
            for i in row:
                text_row += str(i) + ' '
            text_file.write(text_row + '\n')
        text_file.write('\n')
    text_file.close()

optimal_designs = compute_optimal_designs(3, 5)
save_optimal_designs(optimal_designs)

print('END')