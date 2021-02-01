#coding:utf-8

class Numone:
    def __init__(self,num):
        self.num = round(num,1)

    def __str__(self):
        return "{0:.1f}".format(self.num)

    __repr__=__str__

n = Numone(6.8888)
print(n)