################################# 1-misol ########################################
##Create a vector with values ranging from 10 to 49.
# import numpy as np
# vector = np.arange(10, 50)
# print(vector)
################################# 2-misol ########################################
##Create a 3x3 matrix with values ranging from 0 to 8.
# import numpy as np
# matrix = np.arange(9).reshape(3, 3)
# print(matrix)
################################# 3-misol ########################################
##Create a 3x3 identity matrix.
# import numpy as np
# identity_matrix = np.identity(3)
# print(identity_matrix)
################################# 4-misol ########################################
## Create a 3x3x3 array with random values.
# import numpy as np
# random_array = np.random.rand(3, 3, 3)
# print(random_array)
################################# 5-misol ########################################
## Create a 10x10 array with random values and find the minimum and maximum values.
# import numpy as np
# array_10x10 = np.random.rand(10, 10)
# min_value = np.min(array_10x10)
# max_value = np.max(array_10x10)
# print("Array:\n", array_10x10)
# print("\nMinimum value:", min_value)
# print("Maximum value:", max_value)
################################# 6-misol ########################################
## Create a random vector of size 30 and find the mean value.
# import numpy as np
# random_vector = np.random.rand(30)
# mean_value = np.mean(random_vector)
# print("Random Vector:\n", random_vector)
# print("\nMean Value:", mean_value)
################################# 7-misol ########################################
## Normalize a 5x5 random matrix.
# import numpy as np
# matrix = np.random.rand(5, 5)
# normalized_matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))
# print("Original Matrix:\n", matrix)
# print("\nNormalized Matrix:\n", normalized_matrix)
################################# 8-misol ########################################
## Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
# import numpy as np
# A = np.random.rand(5, 3)
# B = np.random.rand(3, 2)
# result = np.dot(A, B)  
# print("Matrix A (5x3):\n", A)
# print("\nMatrix B (3x2):\n", B)
# print("\nMatrix Product (5x2):\n", result)
################################# 9-misol ########################################
## Create two 3x3 matrices and compute their dot product.
# import numpy as np
# A = np.random.rand(3, 3)
# B = np.random.rand(3, 3)
# dot_product = np.dot(A, B)  
# print("Matrix A:\n", A)
# print("\nMatrix B:\n", B)
# print("\nDot Product (A · B):\n", dot_product)
################################# 10-misol #######################################
## Given a 4x4 matrix, find its transpose.
# import numpy as np
# matrix = np.random.rand(4, 4)
# transpose_matrix = matrix.T
# print("Original Matrix (4x4):\n", matrix)
# print("\nTranspose of the Matrix (4x4):\n", transpose_matrix)
################################# 11-misol #######################################
## Create a 3x3 matrix and calculate its determinant.
# import numpy as np
# matrix = np.random.rand(3, 3)
# determinant = np.linalg.det(matrix)
# print("Matrix (3x3):\n", matrix)
# print("\nDeterminant of the Matrix:", determinant)
################################# 12-misol #######################################
## Create two matrices ( A ) (3x4) and ( B ) (4x3), and compute the matrix product ( A \cdot B ).
# import numpy as np
# A = np.random.rand(3, 4)
# B = np.random.rand(4, 3)
# matrix_product = np.dot(A, B)  
# print("Matrix A (3x4):\n", A)
# print("\nMatrix B (4x3):\n", B)
# print("\nMatrix Product (A · B) (3x3):\n", matrix_product)
################################# 13-misol #######################################
## Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.
# import numpy as np
# matrix = np.random.rand(3, 3)
# vector = np.random.rand(3, 1)
# result = np.dot(matrix, vector)  
# print("Matrix (3x3):\n", matrix)
# print("\nColumn Vector (3x1):\n", vector)
# print("\nMatrix-Vector Product:\n", result)
################################# 14-misol #######################################
## Solve the linear system ( Ax = b ) where ( A ) is a 3x3 matrix, and ( b ) is a 3x1 column vector.
# import numpy as np
# A = np.random.rand(3, 3)
# b = np.random.rand(3, 1)
# x = np.linalg.solve(A, b)
# print("Matrix A (3x3):\n", A)
# print("\nColumn Vector b (3x1):\n", b)
# print("\nSolution Vector x (3x1):\n", x)
################################# 15-misol #######################################
## Given a 5x5 matrix, find the row-wise and column-wise sums.
# import numpy as np
# matrix = np.random.rand(5, 5)
# row_sums = np.sum(matrix, axis=1)
# column_sums = np.sum(matrix, axis=0)
# print("Matrix (5x5):\n", matrix)
# print("\nRow-wise Sums:\n", row_sums)
# print("\nColumn-wise Sums:\n", column_sums)
