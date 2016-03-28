# Matrix Algebra

import numpy as np

# Define matrices
# Matrix
a = np.array([[1, 2, 3], [2, 7, 4]])

# Matrix
b = np.array([[1, -1], [0, 1]])

# Matrix
c = np.array([[5, -1], [9, 1], [6, 0]])

# Matrix
d = np.array([[3, -2, -1], [1, 2, 3]])

# Vector
u = np.array([6, 2, -3, 5])

# Vector
v = np.array([3, 5, -1, 4])

# Matrix
w = np.array([[1], [8], [0], [5]])

print '# 1 Matrices Dimension', '\n'
# 1.1
print 'a dimension:', a.shape, '\n'
# 1.2
print 'b dimension:', b.shape, '\n'
# 1.3
print 'c dimension:', c.shape, '\n'
# 1.4
print 'd dimension:', d.shape, '\n'
# 1.5
print 'u dimension:', u.shape, '\n'
# 1.6
print 'w dimension:', w.shape, '\n'

print '# 2 Vector Operations, alpha = 6', '\n'
alpha = 6

# 2.1
print 'u + v = ', u + v, '\n'
# 2.2
print 'u - v = ', u - v, '\n'
# 2.3
print 'alpha * u = ', alpha * u, '\n'
# 2.4
print 'u * v = ', u * v, '\n'
# 2.5
print 'u norm = ', np.linalg.norm(u), '\n'

print '# 3 Matrix Operations'

# 3.1
print 'a + b ---> not defined, a is a 2 x 3 and b is a 2 x 2 matrix', '\n'
# 3.2
print 'a - c transpose = ', a - np.transpose(c), '\n'
# 3.3
print 'c transpose + 3 * d = ', np.transpose(c) + (3 * d), '\n'
# 3.4
print 'b . a = ', np.dot(b, a), '\n'
# 3.5
print 'b . a transpose ---> not defined, b is a 2 x 2 and a transpose is a 3 x 2 matrix', '\n'

print 'Optional'
# 3.6
print 'b . c ---> not defined, b is 2 x 2 and c is a 3 x 2 matrix', '\n'
# 3.7
print 'c . b = ', np.dot(c, b), '\n'
# 3.8
print 'b raise to the 4', b ** 4, '\n'
# 3.9
print 'a . a transpose = ', np.dot(a, np.transpose(a)), '\n'
# 3.10
print 'd transpose . d = ', np.dot(np.transpose(d), d), '\n'


# # 1 Matrices Dimension
#
# a dimension: (2, 3)
#
# b dimension: (2, 2)
#
# c dimension: (3, 2)
#
# d dimension: (2, 3)
#
# u dimension: (4,)
#
# w dimension: (4, 1)
#
# # 2 Vector Operations, alpha = 6
#
# u + v =  [ 9  7 -4  9]
#
# u - v =  [ 3 -3 -2  1]
#
# alpha * u =  [ 36  12 -18  30]
#
# u * v =  [18 10  3 20]
#
# u norm =  8.60232526704
#
# # 3 Matrix Operations
# a + b ---> not defined, a is a 2 x 3 and b is a 2 x 2 matrix
#
# a - c transpose =  [[-4 -7 -3]
#  [ 3  6  4]]
#
# c transpose + 3 * d =  [[14  3  3]
#  [ 2  7  9]]
#
# b . a =  [[-1 -5 -1]
#  [ 2  7  4]]
#
# b . a transpose ---> not defined, b is a 2 x 2 and a transpose is a 3 x 2 matrix
#
# Optional
# b . c ---> not defined, b is 2 x 2 and c is a 3 x 2 matrix
#
# c . b =  [[ 5 -6]
#  [ 9 -8]
#  [ 6 -6]]
#
# b raise to the 4 [[1 1]
#  [0 1]]
#
# a . a transpose =  [[14 28]
#  [28 69]]
#
# d transpose . d =  [[10 -4  0]
#  [-4  8  8]
#  [ 0  8 10]]