#coding:utf-8
"""
单继承
"""

class person:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def getName(self):
        return self.name
    def getSex(self):
        return self.sex

class student(person):
    def grade(self,grade):

        print ("{name} 是 {sex}孩子，现在上{grade}".format(name = self.name,sex=self.sex,grade=grade))

zhang = student('张三','男')

zhang.grade('四年级')
print(zhang.getName())
print(zhang.getSex())

