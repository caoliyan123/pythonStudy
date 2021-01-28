#coding:utf-8

'''
编写程序，判断用户输入的网站主域名是否符合规定格式
www.xxxx.xxx
'''

web = input('请输入网站域名:')

weblist = web.split('.')



if weblist[0]=='www':
    if len(weblist[1])==4 :
        if len(weblist[2])==3:
            print('网站域名正确')
        else:
            print('网站域名后缀错误')
    else :
        print('机构名错误')
else :
    print('www协议错误')



#c^2=a^2+b^2-2abcosc


import math

a = 3
b = 7
c = 9

cosC = (a*a + b*b - c*c)/(2*a*b)
C = math.acos(cosC)
print(C)

