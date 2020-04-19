from itertools import combinations_with_replacement

from project_math.matrices import compute_all_permutations

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