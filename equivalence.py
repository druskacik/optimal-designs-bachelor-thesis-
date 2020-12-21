import numpy as np

from project_math.matrices import compute_all_binary_matrices
from project_math.variance import compute_transformation_matrix

def test_equality():
  matrices = compute_all_binary_matrices(2, 2)
  for matrix in matrices:
    print(matrix)
    print(compute_transformation_matrix(np.array(matrix)))


test_equality()
