import pymysql
import requests

db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_user')
cursor = db.cursor()
list3 = ['18823303216','13066909086','18565688072','15710838330','18820184744','19930807004']    #省代，市代，城主，AB差，推荐人 代理发红包列表
list4 = ['18823303216','13066909086','18565688072','15710838330','18820184744','19930807004','19930807005']    #省代，市代，城主，AB差，AB差，推荐人,粉丝发红包列表

for i in list4:
    cursor.execute('select token from login_log,user_info where user_account_uuid = user_uuid and mobile = %s' % i)
    data = cursor.fetchone()
    headers = {
        "Accept": "*/*",
        "h-api-token": "%s" % data,
        "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJleHAiOjE1NTM0Nzk1MDAsImlhdCI6MTUzNjE5OTQ5OTkwNn0.P42ZXPgMp8ApbDPKgYvLB-wpLFqK2XbgWbcyMEPCueRIz3FDFZwID3PXe6KHvfES0l7Wq1v45OprxcE9wpqNaw",
        "h-time": "1652356598220",
        "h-tenant-code": "gcyh",
        "h-nonce": "6917b1a82f0a43b5888af48c6a9f4100"
    }
    url = 'http://172.18.228.127:7005/api/v1/user/wallet/coin'
    r = requests.get(url=url, headers=headers).json()
    print(r['response'])
cursor.execute('select income_coin from tenant_wallet where id = 1')
zengzhichi = cursor.fetchone()
cursor.execute('select income_coin from tenant_wallet where id = 2')
gongsizhanghu = cursor.fetchone()
print('增值池：',zengzhichi[0],'\n'
      '公司账户：',gongsizhanghu[0])