import numpy as np

# Convert the following 1-D array with 12 elements into a 2-D array.

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) # 1-d array
newarr = arr.reshape(4,3)  # 2-d array
array3d = arr.reshape(2,3,2)  # 3-d array
print(newarr)
print(array3d)

# array1d = array3d.reshape(12)
array1d = array3d.reshape(-1)
print(array1d)


data = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
data2d = data.reshape(5,-1)
print(data2d)

for x in data:   # itterrating though array
  print(x+10)

# itterating though 2d array
names = np.array( [  ["devraj","mahsim"] ,  ['ronak','atul']  , ['arpt','maulik']  ])

print(names)

for x in names:
  for y in x:
    print(y)

