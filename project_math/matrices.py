import numpy as np

def compute_all_permutations(n, list_of_matrices=[], start=''):
    if n == 1:
        list_of_matrices.append(start + '0')
        list_of_matrices.append(start + '1')
        return list_of_matrices
    list_of_matrices.extend(compute_all_permutations(n - 1, [], start + '0'))
    list_of_matrices.extend(compute_all_permutations(n - 1, [], start + '1'))
    return list_of_matrices
        
def compute_all_binary_matrices(m, n):
    matrices = []
    permutations = compute_all_permutations(m*n)
    for permutation in permutations:
        matrix = np.zeros(shape=(m, n), dtype=np.int8)
        for index, e in enumerate(permutation):
            if (e == '1'):
                matrix[index//n][index%n] = 1
        matrices.append(matrix)
    return matrices

# matrices = compute_all_binary_matrices(2, 3)
# print(len(matrices))
# print(matrices[100])

# a = np.zeros(shape=(2, 4))
# print(a[2][2])