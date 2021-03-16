#coding:utf-8
import numpy as np
import time

num_count=500000

def python_list():
    t_time=time.time()
    x=range(num_count)
    y=range(num_count)
    z=[]
    for i in range(len(x)):
        z.append(x[i] + y[i])
    return time.time()-t_time
t1=python_list()

def numpy_list():
    t2=time.time()
    x=np.array(num_count)
    y=np.array(num_count)
    z=x+y
    return time.time()-t2
t2=numpy_list()

print(t1,t2)