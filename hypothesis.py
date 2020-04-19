import numpy as np

from project_math.matrices import compute_all_binary_matrices
from helpers.save_designs import save_designs
from project_math.bigger_matrices import compute_matrices

def compute_matrices_from_hypothesis(n):
  binary_matrices = compute_all_binary_matrices(n, n)
  matrices = []
  for matrix in binary_matrices:
    if matrix_meets_hypothesis(matrix):
      matrices.append(matrix)
  return matrices

def check_for_bigger_matrices(n):
  binary_matrices = compute_matrices(n, n)
  matrices = []
  for matrix in binary_matrices:
    matrix = np.array(matrix)
    if matrix_meets_hypothesis(matrix):
      matrices.append(matrix)
  return matrices

def matrix_meets_hypothesis(matrix):
  n = matrix.shape[0]
  if n%2 == 0:
    if sum(sum(matrix)) != (n**2)/2:
      return False
    for i, row in enumerate(matrix):
      if sum(row) != n/2 or sum(matrix[:, i]) != n/2:
        return False
  else:
    s = sum(sum(matrix))
    if s != n*(n + 1)/2 and s != n*(n - 1)/2:
      return False
    count_in_row = s/n
    for i, row in enumerate(matrix):
      if sum(row) != count_in_row or sum(matrix[:, i]) != count_in_row:
        return False
  return True

# designs = compute_matrices_from_hypothesis(5)
designs = check_for_bigger_matrices(5)

save_designs('data/from_hypothesis', designs)

print('END')
