# -*- coding:utf-8 -*-

'''
@versoin:1.0
@author:t-bag
@file:content13.py
@time:2018-12-5 20:07:38
'''

c = 'xiaobao'
d = '123456'

def login_port():
    a = input(str('请输入用户名'))
    b = input(str('请输入密码'))
    if a == c and b == d:
        print('%s登录成功' % c)
    elif a == c and b != d:
        print('密码错误')
    elif a != c:
        print('用户名或密码错误')
    else:
        print('服务器错误')

if __name__ == '__main__':
    login_port()
