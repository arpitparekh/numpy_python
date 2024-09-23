import numpy as np
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
"""
# bool_array = np.array([True,False,True],dtype="b")
# print(bool_array.dtype)

bool_array = np.array([True,False,True])
print(bool_array)
print(bool_array.dtype)

num_array = np.array([1,2,3,4,5],dtype="S")
print(num_array)
print(num_array.dtype)

# stringArray = np.array(["Hello","Hi","Kem cho"],dtype="i")  # not possible
# print(stringArray)
# print(stringArray.type)

stringArray2 = np.array(["1","2","3"],dtype="i")
print(stringArray2)
print(stringArray2.dtype)


int_array = np.array([1,2,3,4,5,6,7,8])
print(int_array)
print(int_array.dtype)

new_array =  int_array.astype("S")  # used to chnage the datatype of exsisting array
print(new_array.dtype)
print(new_array)

int_array2 = np.array([1,2,3,4,0,6,0,8])

bool_array = int_array2.astype(bool)
print(bool_array)

bool_copy = bool_array.copy()
print(bool_copy)
bool_copy[0] = False

print("copy function Original",bool_array)
print("copy function Copy",bool_copy)

bool_another_copy = bool_array.view()
print(bool_another_copy)
bool_another_copy[0] = False

# view se banao aur view wale naye array me chnage karo to original array me bhi chnage hoga

print("View function Original",bool_array)
print("View function  Copy",bool_another_copy)


print("Shape of an array",bool_array.shape)  # check size
