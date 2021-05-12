#coding:utf-8

import telnetlib
import time

username='dev'
ip='36.110.98.226'
passwd='admin@123'
usermodtag='>'
sysmontag=']'

try:
    #建立一个连接
    tel=telnetlib.Telnet(ip,port=23)

    login_user=b'Username:'
    response=tel.read_until(login_user)
    if login_user in response:
        print('Username:',username)
    tel.write(username.encode('ascii')+ b'\n')


    password='Password'
    response = tel.read_until(password.encode('ascii'))
    if password.encode('ascii') in response:
        print('Password: ', passwd)
    tel.write(passwd.encode('ascii')+b'\n')


    response = tel.read_until(usermodtag.encode('ascii'))
    if usermodtag.encode('ascii') in response:
        print(response.decode('ascii'))
    time.sleep(2)
    list=tel.write("dis cu | i nat static protocol\n".encode())
    #print(list)
    response = tel.read_until(usermodtag.encode())
    print(response.decode())
    # 测试完毕后，关闭连接
    time.sleep(2)
    # 测试完毕后，关闭连接

except Exception as e:
    print(e)



