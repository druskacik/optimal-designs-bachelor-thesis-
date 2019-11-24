import numpy as np

matrix = [[1, 0], [0, 1]]
matrix = np.array(matrix)

matrix2 = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1]
]
matrix2 = np.array(matrix2)

matrix3 = np.zeros(shape=(3, 5), dtype=np.int8)

matrix4 = np.random.randint(2, size=(4, 4))

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
    fmatrix = np.matmul(transformation_matrix.transpose(), transformation_matrix)
    determinant = np.linalg.det(fmatrix)
    print(determinant)
    try:
        h = np.zeros(shape=(1, m + n + 2))
        h[0, m + n] = 1
        h[0, m + n + 1] = -1
        variance = np.matmul(np.matmul(h, np.linalg.pinv(fmatrix)), h.transpose())
        return variance[0, 0]
    except Exception as e:
        print(e)
        # print('F matrix is singular !')
        return 0

print(matrix4)
variance = compute_variance(matrix4)
print(variance)

print('END')