import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr3=np.concatenate((arr1,arr2))

print(arr3)

arr4 = np.stack((arr1,arr2))

print(arr4)

arr5 = np.hstack((arr1,arr2))

arr6 = np.vstack((arr1,arr2))

print(arr5)
print(arr6)
