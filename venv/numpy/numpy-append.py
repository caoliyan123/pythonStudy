#coding:utf-8
import numpy as np

arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[11,22,33]])

b=np.concatenate((arr1,arr2),axis=0)
print(b)

c=np.vstack((arr1,[22,33,44]))
print(c)
d=np.hstack((arr1,[[221,331,44],[343,55,66]]))
print(d)

print('*'*60)
arr3=np.arange(9).reshape(3,3)
e=np.vsplit(arr3,3)
f=np.hsplit(arr3,3)
print(e)
print(f)

print('*'*30)
g=np.insert(arr1,1,[33,44,55],axis=0)
print(g)

print('*'*30)
h=np.append(arr1,[44,55,66],axis=0)
print(h)