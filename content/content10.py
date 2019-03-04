import pymysql
import re
import string
db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_common')
cursor = db.cursor()
cursor.execute('select code from region where id < 34')
data = cursor.fetchall()
s = (list(data))
print(len(s))

import os
print(os.getcwd())
def t1():
    try:
        for i in range(0,len(s)):
            b = int(((s[i])[0]))
            return b
    except:
        pass
def t2():
    try:
        for i in range(0,len(s)):
            a = int(((s[i])[0]))
            return a
    except:
        pass
a = t1()
b = t2()

def t3():
    if a == b:
        print(a,b,'ok')
    else:
        print(a,b,'o个锤子')


if __name__ == '__main__':
    t3()



