import numpy as np
from itertools import permutations

def permute_by_rows(matrix):
  matrices = []
  permutation_string = ''
  for i in range(len(matrix)):
    permutation_string += str(i)
  perms = permutations(permutation_string)
  for permutation in perms:
    permuted = []
    for index in permutation:
      permuted.append(matrix[int(index)])
    if permuted not in matrices:
      matrices.append(permuted)
  return matrices

def permute_matrix(matrix):
  matrices = []
  permutation_string = ''
  for i in range(len(matrix)):
    permutation_string += str(i)
  perms = permutations(permutation_string)
  for permutation in perms:
    permuted = []
    for index in permutation:
      permuted.append(matrix[int(index)])
    column_permutations = permute_by_rows(np.array(permuted).transpose().tolist())
    for matrix in column_permutations:
      matrix = np.array(matrix).transpose().tolist()
      if matrix not in matrices:
        matrices.append(matrix)
  return matrices