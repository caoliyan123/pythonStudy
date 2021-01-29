#coding:utf-8
"""
创建一个自动处理数据的类，用整数组成的列表作为实例化参数之后，自动将列表中的数字分为奇数和偶数（质数/合数）
"""
class numSplit:
    def __init__(self,numList):
        self.odds = [i for i in numList if i % 2 == 1]
        self.even = [i for i in numList if i % 2 == 0]

lst = [1,2,3,4,5,6]
a = numSplit(lst)
print(a.even)
print(a.odds)

