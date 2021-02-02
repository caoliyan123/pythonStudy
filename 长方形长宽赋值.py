#coding:utf-8

class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    def __getattr__(self, name):
        if name == 'size':
            return self.length ,self.width
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        if name == 'size':
            self.length,self.width = value
        else:
            self.__dict__[name] = value

r = Rectangle()
r.length = 4
r.width = 3
print(r.size)

r.size = 40,30

print(r.width)
print(r.length)