import numpy as np

ar1 = np.array([1, 2, 3])

# ar2 = np.array([[4, 6, 1], [2, 3, 5, 6], [5, 3, 4, 1]])  # VisibleDeprecationWarning: Creating an ndarray from ragged
# nested sequences

ar3 = np.array([[4, 6, 1, 3], [2, 3, 5, 6], [5, 3, 4, 1]], dtype='int64')
print(ar3)

# Get Dimension
print(ar3.ndim)

# Get Shape - Gives Vector
print(ar3.shape)

# Get Type
print(ar3.dtype)

# Get Size
print(ar3.itemsize)

# Get Total Size
print(ar3.nbytes)

# Access Rows,Columns

# Get Specific element - [r,c]
print(ar3[1, 3])

# Get Specific row
print(ar3[1, :])

# Get Specific column
print(ar3[:, 3])

# Initialize all different types of arrays

# All 0's Matrix
print(np.zeros((2, 3, 2, 5)))

# All 1's Matrix
print(np.ones((2, 3, 2, 5), dtype='int16'))

# Any Other Number
print(np.full((2, 3), 77, dtype='int16'))

# Any Other Number with full_like
print(np.full_like(ar3, 77, dtype='int16'))

# Random Decimals
print(np.random.rand(4, 3))

# Random Decimals with Shape
print(np.random.random_sample(ar3.shape))

# Random Integers
print(np.random.randint(7, 10, size=ar3.size))

# identity Matrix
print(np.identity(5))

# Repeat Array
myArr = np.array([[1, 2, 3]])
r1 = np.repeat(myArr, 3, axis=0)
print(r1)

# Problem:
res = np.ones((5, 5))
z = np.zeros((3, 3))
z[1, 1] = 9
res[1:4, 1:4] = z
print(res)

# Careful in Copying
sample = np.array([1, 2, 3])
b = sample.copy()
b[1] = 200
print(b)
print(sample)

# Maths
# https://numpy.org/doc/stable/reference/routines.linalg.html
print(np.sin(sample))

a = np.ones((3, 2))
b = np.full((2, 3), 3)
res = np.matmul(a, b)
print(res)

# Find the Determinant
id = np.identity(3)
print(np.linalg.det(id))

# Statistics
print(np.max(ar3, axis=1))
print(np.sum(ar3))

# Reorganizing
before = np.array([[4, 6, 1, 3], [2, 3, 5, 6]])
after = before.reshape((8, 1))
print(after)

# Vertical Stacking
v1 = np.array([4, 6, 1, 3])
v2 = np.array([2, 3, 5, 6])
print(np.vstack([v1, v2, v2]))

# # Misc
f1 = np.genfromtxt("data.txt", delimiter=",")
f1 = f1.astype("int32")

# Boolean Masking and Advanced Indexing
print([f1 > 50])
np.any(f1 > 50, axis=0)  # Column Indexing
np.all(f1 > 50, axis=0)

# Examples:
a = ar3[2:4, 0:2]
b = ar3[[0, 1, 2, 3], [1, 2, 3, 4]]
c = ar3[[1, 3, 4], 3:]

