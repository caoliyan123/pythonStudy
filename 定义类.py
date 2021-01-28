#coding:utf-8
"""
创建一个反应学生基本属性和方法的类，并实例化
"""
class student:  #
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        self.shuxing = '学生'


zhang = student('hang','男')

zhang.name
zhang.sex