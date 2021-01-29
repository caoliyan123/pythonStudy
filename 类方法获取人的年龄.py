#coding:utf-8

"""
创建一个关于人的类，能够以姓名和年龄作为初始化参数创建实例，此外，还允许以出生年份来创建实例。
分别通过以上两种实例化途径创建实例，都能够以一个方法得到该实例的当前年龄
"""
from datetime import datetime

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def birthday(cls,name,birth):
        today = datetime.today()
        born = datetime.strptime(birth, '%Y-%m-%d')
        age = today.year - born.year
        return  cls(name,age)


a = person('小红',28)
b = person.birthday('小蓝','2019-10-09')
print ('{name} is {birthday} years old'.format(name = a.name,birthday = a.age))
print ('{name} is {birthday} years old'.format(name = b.name,birthday = b.age))
