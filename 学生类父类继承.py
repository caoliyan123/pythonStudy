#coding:utf-8

class SchoolKid:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    #更改年龄，姓名
    def re_age(self,new_age):
        self.age = new_age
        return self.age
    def re_name(self,new_name):
        self.name = new_name
        return self.name
    # 获取年龄，姓名
    def get(self,attr='name'):
        if attr == 'name':
            return self.name
        elif attr == 'age':
            return self.age
        else:
            print('输入错误')

class ExaggeratingKid(SchoolKid):
    def get(self,attr='name'):
        if attr == 'name':
            return self.name
        elif attr == 'age':
            self.age = self.age +2
            return self.age
        else:
            print('输入错误')

s = SchoolKid('Petter',12)

print (s.get('name'))
print (s.get('age'))
print(s.re_name('Tom'))

s1 = ExaggeratingKid('Petter',12)
print(s1.get('name'))
print(s1.get('age'))
print(s.re_name('Tome'))
