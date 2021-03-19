#coding:utf-8

import numpy as np

a = np.array([[1,2,6],[2,5,7],[6,8,4]])
b = np.array([100,80,90])
c = np.linalg.solve(a,b)
print(c)

a=np.array([[1,4],[2,6]])
b=np.linalg.det(a)
print (b)

a=np.matrix('1,2;3,4')
print(a)
b=np.linalg.inv(a)
print(b)

c=a.dot(b)
print(c)