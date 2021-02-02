#coding:utf-8

"""
内置函数range的参数必须是整数。请编写一个生成器函数，以浮点数为参数（开始值，结束值，步长）生成某范围的序列
"""
import itertools

def frange(start,stop=None,step=1):
    if stop is None:
        stop = float(start)
        start = 0.0
    assert step
    for i in itertools.count():
        nxt = start + i * step
        if (step > 0.0 and nxt >= stop) or (step<0.0 and nxt <= stop):
            break
        yield nxt

print(list(frange(1.2,5.8,0.5)))
