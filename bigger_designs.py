import numpy as np
from itertools import combinations_with_replacement

from matrices import compute_all_permutations
from variance import compute_variance
from helpers.minimum_with_indices import min_with_indices

def compute_matrices(number_of_rows, number_of_columns):
  perms = compute_all_permutations(number_of_columns)
  combs = combinations_with_replacement(perms, number_of_rows)
  matrices = []
  for combination in combs:
    matrix = []
    for row in combination:
      matrix_row = []
      for value in row:
        matrix_row.append(int(value))
      matrix.append(matrix_row)
    matrices.append(matrix)
  return matrices

def compute_variances(number_of_rows, number_of_columns):
  binary_matrices = compute_matrices(number_of_rows, number_of_columns)
  variances = []
  for matrix in binary_matrices:
    model_variance = compute_variance(np.array(matrix))
    variances.append(round(model_variance, 3))
  return binary_matrices, variances

def compute_optimal_designs(number_of_rows, number_of_columns):
  matrices, variances = compute_variances(number_of_rows, number_of_columns)
  indices = min_with_indices(variances)
  optimal_designs = []
  for i in indices:
      optimal_designs.append(np.array(matrices[i]))
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

designs = compute_optimal_designs(6, 5)
save_optimal_designs(designs)

print('END')
