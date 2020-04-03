import numpy as np
import math

def compute_transformation_matrix(matrix):
    m, n = matrix.shape
    transformation_matrix = np.zeros(shape=(m*n, m + n + 2), dtype=np.int8)
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            transformation_matrix[n*i + j, i] = 1
            transformation_matrix[n*i + j, m + j] = 1
            transformation_matrix[n*i + j, m + n + value] = 1
    return transformation_matrix

def compute_variance(matrix):
    m, n = matrix.shape
    transformation_matrix = compute_transformation_matrix(matrix)
    m_matrix = np.matmul(transformation_matrix.transpose(), transformation_matrix)
    m_matrix_inverse = np.linalg.pinv(m_matrix)
    # determinant = np.linalg.det(m_matrix)
    # print(determinant)
    try:
        h = np.zeros(shape=(1, m + n + 2))
        h[0, m + n] = 1
        h[0, m + n + 1] = -1
        wannabe_h = np.matmul(np.matmul(m_matrix, m_matrix_inverse), h.transpose())
        for i, value in enumerate(wannabe_h):
            wannabe_h[i] = [round(value[0], 3)]
        if np.array_equal(wannabe_h, h.transpose()):
            variance = np.matmul(np.matmul(h, m_matrix_inverse), h.transpose())
            return variance[0, 0]
        else:
            return math.inf
    except Exception as e:
        print(e)
        # print('F matrix is singular !')
        return math.inf