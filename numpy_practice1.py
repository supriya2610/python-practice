'''import numpy as np
arr=np.array([[1,3,4,5,7],[2,5,7,3,8]])
print(arr.shape)
x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)'''
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)
