import pymysql
import requests
import json

def get_city():
    db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_common')
    cursor = db.cursor()
    cursor.execute('select code from region where id < 34' )
    data = cursor.fetchall()
    aaa = list(data)

def get_id_count(a):
    db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_common')
    cursor = db.cursor()
    cursor.execute('select count(*) from region where parent_id = %s' % a)
    data = cursor.fetchone()
    print('数据库个数',(data)[0])
    a = data[0]
    yyy = int(a)
    bijiao(yyy)


def get_id(a):
    url = 'https://apis.map.qq.com/ws/district/v1/getchildren'
    data = {'id':'%s' % a,'key':'RDJBZ-YTZR2-CJJUT-CXLNZ-2SPV6-PBBJY'}
    r = requests.get(url = url,params = data).json()
    a = r['result']
    b = a[0]
    print('接口个数',len(b))
    c = len(b)
    zzz = int(c)
    bijiao(zzz)


def bijiao(zzz,yyy):
    if int(zzz) == int(yyy):
        print('对的')


if __name__ == '__main__':
    get_city()

