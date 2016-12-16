# Matrix Algebra
import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])

B = np.array([[1, -1], [0, 1]])

C = np.array([[5, -1], [9, 1], [6, 0]])

D = np.array([[3, -2, -1], [1, 2, 3]])

u = np.array([[6, 2, -3, 5]])

v = np.array([[3, 5, -1, 4]])

w = np.array([[1], [8], [0], [5]])

#1. Matrix Dimensions
print A.shape
print B.shape
print C.shape
print D.shape
print u.shape
print w.shape

#2. Vector Operations
print u + v
print u - v
print 3 * u
print u * v
print np.linalg.norm(u)

#3. Matrix Operations
#print A + C = Not Defined
print A - C.T
print C.T + 3*D
print B.dot(A)
#print B * A.T = Not Defined

#4. Optional
#print B.dot(C) = Not Defined
print C.dot(B)
print np.power(B, 4)
print A.dot(A.T)
print (D.T).dot(D)

