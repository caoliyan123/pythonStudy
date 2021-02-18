#coding:utf-8
"""
创建一个反应学生基本属性和方法的类，并实例化
"""
class student:  #
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        self.shuxing = '学生'
    def eat(self,food):
        if food == 'meat':
            price = 10
            return price
        else:
            price=5
            return price
    def learn(self,*subject):
        if 'python' in subject:
            return ('前程似锦')
        else:
            return ('加油努力')


zhang = student('hang','男')
b = zhang.eat('meat')
c = zhang.learn('python','english','math','chinese')

print(zhang.name)
print(zhang.sex)
print(b)
print(c)
