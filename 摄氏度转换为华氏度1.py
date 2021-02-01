#coding:utf-8

class Celsius:
    def __init__(self,temperature):
        self.temperature = temperature

    def to_huashe(self):
        hua = (self.temperature * 1.8) + 32
        return  hua

c = Celsius(30)
print ('{c}C = {f}F'.format(c=c.temperature,f=c.to_huashe()))
