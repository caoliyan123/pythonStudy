#coding:utf-8
import numpy as np
import timeit
n=100
print(timeit.timeit(f'x = [x**2 for x in range({n})]'))
print(timeit.timeit(f'x = np.arange({n})**2',setup='import numpy as np'))