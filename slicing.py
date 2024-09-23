import numpy as np


# array is a group of similar type of datatype

arr = np.array([1,2,3,4,5])

print(arr)

arr1 = arr[2:5]  # slicing using : operator
arr2 = arr[3:]
arr3 = arr[:2]
arr4 = arr[-3:-1] # not recomended
print(arr1)
print(arr2)
print(arr3)
print(arr4)

data = np.array([1,2,3,4,5,6,7,8])

print(data[0:6:2])  # start:stop:step

dim2 = np.array([ [1,2,3] , [4,5,6]  , [7,8,9] ])
# print(dim2[0:2,2])
print(dim2[0:2,0:2])

# 3,6,9
print(dim2[0:3,2])
