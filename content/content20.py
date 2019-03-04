import pymysql
import requests

db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_user')
cursor = db.cursor()
updatecoin = db.cursor()
#updatecoin.execute('update tenant_wallet set income_coin = 0 where id = 1 or id = 2')
list1 = ['18823303216','13066909086','18927480233','15710838330','18820184744','19930807004','19930807005']    #省代，市代，城主，AB差，推荐人 发红包列表
list2 = ['18823303216','13066909086','18927480233','15710838330','18820184744','19930807004','19930807005']    #省代，市代，城主，AB差，AB差，推荐人,粉丝发红包列表
list3 = ['18823303216','13066909086','18927480233','15710838330','13751113926','18927480233','19930807000',
         '19930807001','19930807002','19930807003','19930807006',
         '19930807007','19930807008','19930807009']     #九级代理
a = '13751113926' #飞哥账号，代理
list5 = ['15710838330','17665329688','18820184744','19930807004','19930807005','19930807012']
list6 = ['15710838330','13751113926','13410340103','19930807014']
list7 = ['15710838330','13751113926','18927480233','19930807017']
list8 = ['15710838330','13751113926','18927480233','19930807000',
         '19930807001','19930807002','19930807003','19930807006',
         '19930807007','19930807008']
list9 = ['15710838330','13751113926']
list10 = ['15710838330','13751113926','18927480233','19930807000',
         '19930807001','19930807002','19930807022']
list11 = ['15710838330','13751113926','18927480233','19930807017','19930807018','19930807027']
list12 = ['19930808000','19930808001','19930808002','19930808019','19930808020','19930808021','19930808035',
          '19930808036','19930808041','19930808042','19930808043','19930808044']
for i in list12:
    headers = {
        "Accept": "*/*",
        "h-api-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhcGlfdXVpZCIsImgtdGVuYW50LWNvZGUiOiJnY3loIiwiZXhwIjoxNTUzNDc5NTAxLCJpYXQiOjE1MzYxOTk1MDE1Nzl9.TSK-6YKhnzX8ZfLN7hyjSAEiTKwHZPZAYyt0Sv6yRWlUmAMVHeYe68XRau69gDl-PlDoHNLUTvpWBeou4bY_sA",
        "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJleHAiOjE1NTM0Nzk1MDAsImlhdCI6MTUzNjE5OTQ5OTkwNn0.P42ZXPgMp8ApbDPKgYvLB-wpLFqK2XbgWbcyMEPCueRIz3FDFZwID3PXe6KHvfES0l7Wq1v45OprxcE9wpqNaw",
        "h-time": "1552356598220",
        "h-tenant-code": "gcyh",
        "h-nonce": "6917b1a82f0a43b5888af48c6a9f4100"
    }
    host = 'http://172.18.228.127:7005/'
    path = 'api/v1/user/account/login'
    url = ''.join([host, path])
    data = {"username": '%s' % i, "password": 123456, "systemCode": 1, "loginType": 1}
    r1 = requests.post(url=url, data=data, headers=headers).json()
    #print(r1)
    a = r1['response']
    headers1 = {
        "Accept": "*/*",
        "h-api-token": "%s" % a,
        "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJleHAiOjE1NTM0Nzk1MDAsImlhdCI6MTUzNjE5OTQ5OTkwNn0.P42ZXPgMp8ApbDPKgYvLB-wpLFqK2XbgWbcyMEPCueRIz3FDFZwID3PXe6KHvfES0l7Wq1v45OprxcE9wpqNaw",
        "h-time": "1652356598220",
        "h-tenant-code": "gcyh",
        "h-nonce": "6917b1a82f0a43b5888af48c6a9f4100"
    }
    url1 = 'http://172.18.228.127:7005/api/v1/user/wallet/coin'
    r = requests.get(url=url1, headers=headers1)
    #print(r.json())
    cursor.execute('select role from user_invite as a,user_info as b where a.user_account_uuid = b.user_account_uuid and mobile = %s' % i)
    role = int(cursor.fetchone()[0])
    if role == 2:
        print('%s：' % i, '我真的是经理：', r.json()['response'])
    elif role == 1:
        if role == 1 and i == '18823303216':
            print(i,'我是省代和代理：', r.json()['response'])
        print('%s：' % i, '我只是个代理：', r.json()['response'])
    elif role == 3:
        print('%s：' % i, '老子是总监：', r.json()['response'])
    elif role == 0 and i == '13066909086':
        print('%s：' % i, '市级代理：', r.json()['response'])
    elif role == 0 and i == '18565688072':
        print('%s：' % i, '城主：', r.json()['response'])
    elif role == 0:
        print('%s：' % i, '俺是粉丝：', r.json()['response'])
    elif role == 4:
        print('%s：' % i, '五星总监：', r.json()['response'])
cursor.execute('select income_coin from tenant_wallet where id = 1')
zengzhichi = cursor.fetchone()
cursor.execute('select income_coin from tenant_wallet where id = 2')
gongsizhanghu = cursor.fetchone()
print('增值池：', zengzhichi[0], '\n'
                             '公司账户：', gongsizhanghu[0])