import numpy as np
from itertools import permutations, combinations
import matplotlib.pyplot as plt

from project_math.variance import compute_variance, compute_transformation_matrix
from helpers.optimal_matrix import create_optimal_matrix

def compute_up_to_dimension(n):
  variances = []
  for i in range(2, n):
    mat = create_optimal_matrix(i)
    mat = np.array(mat)
    variance = compute_variance(mat)
    variances.append(variance)
    print('Dimension ' + str(i) + ': ' + str(round(variance, 3)))
  plt.figure(figsize=(7, 2))
  plt.plot(variances, 'rx')


def is_local_minimum(n):
  variances = []
  matrix = create_optimal_matrix(n)
  v = compute_variance(np.array(matrix))
  # variances.append(compute_variance(np.array(matrix)))
  for i in range(n):
    for j in range(n):
      mat = np.array([row for row in matrix])
      mat[i, j] = 1 - mat[i, j]
      variances.append(compute_variance(mat))
  print(v < min(variances))
  return variances

def compute_information_matrix(matrix):
  transformation_matrix = compute_transformation_matrix(matrix)
  information_matrix = np.matmul(transformation_matrix.transpose(), transformation_matrix)
  return information_matrix

def test_hypothesis(n):
  for i in range(2, n):
    dimension = 2*i
    print('Testing dimension ', dimension)
    matrix = create_optimal_matrix(dimension)
    M = compute_information_matrix(np.array(matrix))

    hT = [0 for i in range(M.shape[0])]
    hT[len(hT) - 2] = -0.5
    hT[len(hT) - 1] = 0.5
    hT = np.array(hT)

    val = np.matmul(np.matmul(hT, M), np.transpose(hT))
    print(1/val)
    print(np.matmul(hT, M))
    print(compute_variance(np.array(matrix)))

# test_hypothesis(5)

s = ''

for i in range(2, 17):
  matrix = create_optimal_matrix(i)
  # print('Dimension ', 2*i)
  d = compute_variance(np.array(matrix))
  print((i, round(d, 4)))
  s += str((i, round(d, 5)))
  # F = compute_transformation_matrix(np.array(matrix))
  # M = compute_information_matrix(np.array(matrix))
  # print(F)
  # print(M)

print(s)

# for i in range(20, 30):
#   v = is_local_minimum(i)

# compute_up_to_dimension(10)
# plt.show()