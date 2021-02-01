#coding:utf-8

class Celsius:
    def __init__(self,temperature = 0):

        self.temperature = temperature

    def to_huashe(self):
        return (self.__temperature * 1.8) + 32


    @property
    def temperature(self):
        print("get temperature")
        return self.__temperature

    @temperature.setter
    def temperature(self,value):
        if value < -273.15:
            raise ValueError('最低温度不应低于-273.15度')
        print ('set value')
        self.__temperature = value

t = Celsius(-210)
#.__temperature(-300)
print(t.__dict__)
print ('{c}C = {f}F'.format(c=t.temperature(-210),f=t.to_huashe()))
