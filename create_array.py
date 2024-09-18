import numpy as np

# create array in numpy

# 0d array
arr0d = np.array(12)

# 1d array
arr1d = np.array([1,2,3,4,5])

# 2d array
arr2d = np.array([ [1,2,3] , [4,5,6] ])   # matrix
print(arr2d[1][0])
print(arr2d[1,0])

"""  2*3 matrix
1 2 3
4 5 6
"""

print(arr0d)
print(arr0d.ndim)  # check dimention
print(arr1d)
print(arr1d.ndim)
print(arr2d)
print(arr2d.ndim)

another_array = np.array([1,2,3,4,5],ndmin = 3)
print(another_array)
