import numpy as np

"""array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])
print(array1 + array2)
print(array1 - array2)
print(array1 * array3 * array2)
print(array1 / array3)"""

#b = np.array([[1.0,2.0,3.0],[3.0,4.0,5.0]])
#print(b)

a = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
b = np.max(a, axis=1).sum()
print(b)
print(np.max(a, axis=1))