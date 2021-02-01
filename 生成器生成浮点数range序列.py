#coding:utf-8

"""
内置函数range的参数必须是整数。请编写一个生成器函数，以浮点数为参数（开始值，结束值，步长）生成某范围的序列
"""
import itertools

def frange(start,stop,step):
    while True:

        start,stop = start,start + step
        yield stop

print(list(frange(1.2,5.8,0.5)))
