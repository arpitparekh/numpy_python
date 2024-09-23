import numpy as np

# group of similar type of element

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

arr3 = np.array([1,2,3,4,5,6,7,8])

new_array = np.split(arr3,4)

print(new_array)

arr4 = np.array([1,2,3,4])

new_array2 = np.array_split(arr4,3)   # split the array into 3 parts

print(new_array2[0])
