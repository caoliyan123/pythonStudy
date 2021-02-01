#coding:utf-8

"""
使用生成器编写斐波那契数列
"""
import itertools

def feb():
    fir,sec = 0,1
    while True:
        fir,sec = sec , fir+sec
        yield fir

print(list(itertools.islice(feb(),10)))