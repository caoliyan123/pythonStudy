#coding:utf-8

import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
b=a.flatten()
print(b)
b[0]=99
print(b)
print(a)

c=a.ravel()
print(c)
c[0]=99
print(c)
print(a)
print('*'*50)

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=a.transpose()
print(b)
c=np.swapaxes(a,0,1)
print(c)

print('='*50)
a=np.array([[[1,2,3],[4,5,6]],[[10,11,12],[13,14,15]]])
print(a)
b=a.transpose()
print(b)
c=a.swapaxes(1,2)
print(c)