#coding:utf-8
import math

class numSplit:
    def __init__(self, numList):
        self.prime = [i for i in numList if numSplit.primeCompositeSplit(i) == '合数']
        self.composite = [i for i in numList if numSplit.primeCompositeSplit(i) == '质数']

    @staticmethod
    def primeCompositeSplit(x):
        if x < 0:
            return False
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                return '合数'
            else:
                return '质数'


lst = [1,3,2,4,5,13,15,29,30]
a = numSplit(lst)

print(a.prime)
print(a.composite)