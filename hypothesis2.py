import numpy as np

from helpers import permute_matrix
from project_math.variance import compute_transformation_matrix, compute_variance

def random_matrix(n):
  matrix = []
  for i in range(n):
    row = []
    for j in range(n):
      row.append(0 if np.random.random() > 0.5 else 1)
    matrix.append(row)
  return matrix

def compute_information_matrix(matrix):
  f = compute_transformation_matrix(matrix)
  inf = np.matmul(f.transpose(), f)
  # mtm = np.matmul(inf, np.linalg.pinv(inf))
  mm = np.linalg.pinv(inf)
  mm = np.around(mm, 3)
  return [inf.tolist(), mm.tolist()]

def remove_duplicates(arr):
  new_arr = []
  for e in arr:
    if e not in new_arr:
      new_arr.append(e)
  return new_arr

def compare_inverses(matrix):
  matrices = permute_matrix(matrix)
  information_matrices = []
  inverses = []
  for m in matrices:
    [inf, mtm] = compute_information_matrix(np.array(m))
    information_matrices.append(inf)
    inverses.append(mtm)
  n = len(inverses[0])
  print(len(inverses))
  reduced_inverses = remove_with_duplicated_last_square(inverses, n)
  print(len(reduced_inverses))
  print(len(information_matrices))
  reduced_infs = remove_with_duplicated_rows(information_matrices, n)
  # return reduced_inverses
  return reduced_infs

def remove_with_duplicated_last_square(arr, n):
  reduced = []
  squares = []
  for m in arr:
    square = []
    for [i, j] in [[1, 1], [1, 2], [2, 1], [2, 2]]:
      square.append(m[n - i][n - j])
    if square not in squares:
      squares.append(square)
      reduced.append(m)
  return reduced

def remove_with_duplicated_rows(arr, n):
  reduced = []
  rows1 = []
  rows2 = []
  for m in arr:
    if m[n - 2] not in rows1 and m[n - 1] not in rows2:
      rows1.append(m[n - 2])
      rows2.append(m[n - 1])
      reduced.append(m)
  return reduced

matrix = random_matrix(4)

print(matrix)

r = compare_inverses(matrix)
for i in r:
  print(np.array(i))



