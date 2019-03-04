import pymysql
import requests

db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_user')
cursor = db.cursor()
listzh = ['15710838330','13751113926','18927480233','19930807000','19930807001','19930807002','19930807003']
list3 = ['18823303216','13066909086','18565688072','15710838330','18820184744','19930807004']    #省代，市代，城主，AB差，推荐人 代理发红包列表
list2 = ['18823303216','13066909086','18565688072']
for i in list3:
    cursor.execute('select token from login_log,user_info where user_account_uuid = user_uuid and mobile = %s' % i)
    data = cursor.fetchone()
    #print(data)
    headers = {
                "Accept": "*/*",
                "h-api-token": "%s" % data,
                "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJleHAiOjE1NTM0Nzk1MDAsImlhdCI6MTUzNjE5OTQ5OTkwNn0.P42ZXPgMp8ApbDPKgYvLB-wpLFqK2XbgWbcyMEPCueRIz3FDFZwID3PXe6KHvfES0l7Wq1v45OprxcE9wpqNaw",
                "h-time": "1652356598220",
                "h-tenant-code": "gcyh",
                "h-nonce": "6917b1a82f0a43b5888af48c6a9f4100"
    }
    url = 'http://172.18.228.127:7005/api/v1/user/wallet/coin'
    r = requests.get(url = url,headers = headers)
    print(r.json())
    cursor.execute('select role from user_invite as a,user_info as b where a.user_account_uuid = b.user_account_uuid and mobile = %s' % i)
    role = int(cursor.fetchone()[0])
    if role == 2:
        print('%s：' % i,'我真的是经理：',r.json()['response'])
    elif role == 1:
        print('%s：' % i,'我只是个代理：', r.json()['response'])
    elif role == 3:
        print('%s：' % i,'老子是总监：', r.json()['response'])

    #print('%s：'% i,r.json()['response'])
    #print('{}:{}'.format(i,r.json()['response']))
