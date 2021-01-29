#coding:utf-8

"""
创建一个关于人的类，能够以姓名和年龄作为初始化参数创建实例，此外，还允许以出生年份来创建实例。
分别通过以上两种实例化途径创建实例，都能够以一个方法得到该实例的当前年龄
"""
from datetime import datetime

class person:
    def __init__(self,name,**kwargs):
        self.name = name
        self.age = kwargs.get('age')
        self.birth = kwargs.get('birth')
    def birthday(self):
        if self.age:
            return self.age
        if self.birth:
            today = datetime.today()
            born = datetime.strptime(self.birth, '%Y-%m-%d')
            age = today.year - born.year
            return  age
        else:
            return  None

a = person('小红',age=28)
b = person('小蓝',birth='2019-10-09')
print ('{name} is {birthday} years old'.format(name = a.name,birthday = a.birthday()))
print ('{name} is {birthday} years old'.format(name = b.name,birthday = b.birthday()))
