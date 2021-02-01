#coding:utf-8

"""
斐波那契数列
"""

class Fabs:
    def __init__(self,max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __index__(self):
        Fabs = self.a
        if Fabs > self.max:
            raise StopIteration
        self.a,self.b = self.b,self.a+self.b
        return Fabs

f = Fabs(10000)
lst = [f.__index__() for i in range(10)]
print(lst)

