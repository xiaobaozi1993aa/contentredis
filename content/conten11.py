import pymysql
import requests
db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_common')
cursor = db.cursor()
cursor.execute('select code,name from region where id <511')
data = cursor.fetchall()
s = (list(data))
print(len(s))


try:
    for i in range(0,len(s)):
        #b = int(((s[i])[0]))
        a = int(((s[i])[0]))
        cc = (s[i])[1]
        url = 'https://apis.map.qq.com/ws/district/v1/getchildren'
        data = {'id': '%d' % a, 'key': 'RDJBZ-YTZR2-CJJUT-CXLNZ-2SPV6-PBBJY'}
        r = requests.get(url=url, params=data).json()
        aa = r['result']
        b = len(aa[0])
        db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_common')
        cursor = db.cursor()
        cursor.execute('select count(*) from region where parent_id = %d' % a)
        data = cursor.fetchone()
        a = int(data[0])
        if a == b:
            print(cc,'数据库个数:',a,'接口个数:',b,'ok')
        if a != b:
            with open('error.txt','w',encoding='utf-8') as f:
                f.write('报错   ：'+cc+'\r\n')
                f.close()
            print(cc,'数据库个数:',a,b,'接口个数:''--------------------------------ojbk')
except KeyError as a:
    print(str(a))
