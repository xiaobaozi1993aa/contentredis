import redis
import pymysql
import requests

for b in range(19930808110,19930808120):
    a = str(b)
    db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_user')
    cursor = db.cursor()
    cursor.execute('select user_account_uuid from user_info where mobile = %s' % a)
    data1 = cursor.fetchone()
    a = data1[0]

    headers = {
      "Accept": "*/*",
      "h-api-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhcGlfdXVpZCIsImgtdGVuYW50LWNvZGUiOiJnY3loIiwibG9naW5JZCI6ImFwaV91dWlkIiwiZXhwIjoxNTYyMDUwNTcyLCJpYXQiOjE1NDQ3NzA1NzE1MzN9.ig2c4If9Z0Ud4YI-V_eihzjSSvOr1eYteYUvNd0Yd28w5ZHEpTZpYQR2M-MTXCpkgu2i0GXuuoaCEuru5TSRtg",
      "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJsb2dpbklkIjoiYWRtaW5fdXVpZCIsImV4cCI6MTU2MjE1MDI1MCwiaWF0IjoxNTQ0ODcwMjQ2NTMxfQ.kMySAJzhzB-lFkhliSh2S1nYGQMaug2JIPs2ugShZU1wTTcV4n4Edb2pOHgvaRGMSe4Gj6S82BggkVYobu-j1g",
      "h-time": "1555704427313",
      "h-tenant-code": "gcyh",
      "h-nonce": "6a2d12332b1045a6bd968ac17575272a"
    }
    host = 'http://172.18.228.127:7005/api/v1/user/admin/invite/add_inviter'
    data = {'userAccountUuid':data1,'inviteCode':13066909086}
    print(a)
    print(data)
    r = requests.post(url = host,data = data,headers = headers).json()
    print(b,r)