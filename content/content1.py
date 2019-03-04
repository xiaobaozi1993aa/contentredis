import redis
import pymysql
import requests
import re

def get_mysql():
    try:
        db = pymysql.Connect('172.18.228.112','root','3nOI9ca45%$#8Gm7EH','gcyh_sms')
        cursor = db.cursor()
        cursor.execute('select content from send where mobile = "13048818475"')
        data = cursor.fetchone()
        string = str(data)[15:21]
        #print(data)
        #print(type(data))
        print(string)
        #print(type(string))
    except:
        print('获取验证码失败')

if __name__ == '__main__':
    get_mysql()