import numpy as np
"""
Why NumPy?
Fixed type
Low memory
Contiguous Memory
• SIMD single instruction multiple data vector processing
• Effective Cache Utilization
"""
"""
# Creating Numpy array 1,2,3
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])
print(array1 + array2) # adding two arrays each element
print(array1 - array2) # subtracting
print(array1 * array3 * array2) # multiplying
print(array1 / array3) # dividing
"""

#b = np.array([[1.0,2.0,3.0],[3.0,4.0,5.0]])
#print(b)

a = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
b = np.max(a, axis=1).sum() # maximum value in each array axis = 1, axis = 0 means max value in entire array
print(b)
print(np.max(a, axis=1)) # just direct printing nothing fancy