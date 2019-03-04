import requests


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
url = ''.join([host,path])

phone1 = ['19930807000','19930807001','19930807002','19930807003',
          '19930807004']
phone2 = ['15710838330','13751113926','18927480233','17665329688',
          '18820184744','18823303216','13410340103','13048818475',
          '13651494743']
list3 = ['18823303216','13066909086','18565688072','15710838330','18820184744','19930807004']    #省代，市代，城主，AB差，推荐人 代理发红包列表

for i in phone1:
    data = {"username": '%s' % i, "password": 199308, "systemCode": 1, "loginType": 1}
    r = requests.post(url=url, data=data, headers=headers).json()
    print(i,r['message'])

for i in phone2:
    data = {"username": '%s' % i, "password": 123456, "systemCode": 1, "loginType": 1}
    r1 = requests.post(url=url, data=data, headers=headers).json()
    print(i,r1['message'])

for i in phone2:
    data = {"username": '%s' % i, "password": 123456, "systemCode": 1, "loginType": 1}
    r1 = requests.post(url=url, data=data, headers=headers).json()
    a = r1['response']
    print(i,a)