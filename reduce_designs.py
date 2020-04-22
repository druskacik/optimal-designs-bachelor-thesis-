import numpy as np
from itertools import permutations

from helpers.save_designs import save_designs
from helpers.permute_matrix import permute_matrix

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

designs = read_matrices(6, 4)
reduced = reduce_matrices(designs)
save_designs('data/optimal_designs/reduced', np.array(reduced))

print('END')