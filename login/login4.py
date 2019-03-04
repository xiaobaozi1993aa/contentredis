import redis
import pymysql
import requests

for b in range(19930808167,19930808170):
    a = str(b)
    headers = {
                  "Accept": "*/*",
                  "h-api-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhcGlfdXVpZCIsImgtdGVuYW50LWNvZGUiOiJnY3loIiwibG9naW5JZCI6ImFwaV91dWlkIiwiZXhwIjoxNTYyMDUwNTcyLCJpYXQiOjE1NDQ3NzA1NzE1MzN9.ig2c4If9Z0Ud4YI-V_eihzjSSvOr1eYteYUvNd0Yd28w5ZHEpTZpYQR2M-MTXCpkgu2i0GXuuoaCEuru5TSRtg",
                  "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJsb2dpbklkIjoiYWRtaW5fdXVpZCIsImV4cCI6MTU2MjE1MDI1MCwiaWF0IjoxNTQ0ODcwMjQ2NTMxfQ.kMySAJzhzB-lFkhliSh2S1nYGQMaug2JIPs2ugShZU1wTTcV4n4Edb2pOHgvaRGMSe4Gj6S82BggkVYobu-j1g",
                  "h-time": "1555554375874",
                  "h-tenant-code": "gcyh",
                  "h-nonce": "6a669a27a7f04ee0a9df70206195de52"
                }
    host = 'http://172.18.228.127:7005/'
    path4 = 'api/v1/user/account/login'
    url6 = ''.join([host, path4])
    data4 = {"username": a, "password": 123456, "systemCode": 1, "loginType": 0}
    # print('登录数据:', data4)
    r6 = requests.post(url=url6, data=data4, headers=headers).json()
    token1 = r6['response']
    #print('登录数据返回:', r6)
    headers1 = {
        "Accept": "*/*",
        "h-api-token": token1,
        "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJsb2dpbklkIjoiYWRtaW5fdXVpZCIsImV4cCI6MTU2MjE1MDI1MCwiaWF0IjoxNTQ0ODcwMjQ2NTMxfQ.kMySAJzhzB-lFkhliSh2S1nYGQMaug2JIPs2ugShZU1wTTcV4n4Edb2pOHgvaRGMSe4Gj6S82BggkVYobu-j1g",
        "h-time": "1555554375874",
        "h-tenant-code": "gcyh",
        "h-nonce": "6a669a27a7f04ee0a9df70206195de52"
        }
    print(token1)
    path1 = '/api/v1/user/agent/upgrade_agent'
    data1 = {'channelCode':'ios','payType':'11','originalMoney':499}
    url1 = ''.join([host, path1])
    r1 = requests.post(url=url1,data=data1,headers=headers1).json()
    print(a,r1)