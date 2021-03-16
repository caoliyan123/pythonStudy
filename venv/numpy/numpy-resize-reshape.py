#coding:utf-8
import numpy as np

a=np.arange(8)
print(a)

b=a.reshape(2,4)
print(b)
print(b.shape)

c=np.resize(a,(3,6))
print(c)
print(c.shape)