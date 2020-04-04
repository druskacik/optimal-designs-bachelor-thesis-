import numpy as np
from itertools import permutations

from helpers.save_designs import save_designs

def read_matrices(m, n):
  filename = 'data/optimal_designs/designs' + str(m) + 'x' + str(n) + '.txt'
  matrices = []
  with open(filename) as f:
    matrix = []
    for line in f:
      if line[0] == 'D':
        matrices.append(matrix)
        matrix = []
      elif line[0] == '0' or line[0] == '1':
        row = []
        for char in line:
          if char == '0' or char == '1':
            row.append(int(char))
        matrix.append(row)
    matrices.append(matrix)
  return matrices[1:]

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

# beta
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

def reduce_matrices(matrices):
  reduced = []
  def reduce_array(matrices):
    if len(matrices) == 0:
      return
    matrix = matrices[0]
    reduced.append(matrix)
    perms = permute_matrix(matrix)
    for permuted in perms:
      if permuted in matrices:
        matrices.remove(permuted)
    return reduce_array(matrices)
  reduce_array(matrices)
  return reduced

designs = read_matrices(3, 7)
reduced = reduce_matrices(designs)
save_designs('data/optimal_designs/reduced', np.array(reduced))

print('END')