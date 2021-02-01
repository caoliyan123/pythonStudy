#coding:utf-8

class SchoolKid:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_nameage(self):
        return '{name} is {age} years old'.format(name=self.name,age=self.age)


    def age_add(self,val):
        return self.age + val

class ExaggeratingKid(SchoolKid):
