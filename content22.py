import requests
list12 = ['18820184744','13066909086','17665329688','18128823781','19930808101']
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
    # print(r1)
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
    if i == '17665329688':
        print('%s：' % i, '我是市代，我有：', r.json()['response'],'KSB')
    if i == '13066909086':
        print('%s：' % i, '我是城主，我有：', r.json()['response'],'KSB')
    if i == '18820184744':
        print('%s：' % i, '我是上级，我有：', r.json()['response'],'KSB')
    if i == '18128823781':
        print('%s：' % i, '我是省级，我有：', r.json()['response'],'KSB')
    if i == '19930808101':
        print('%s：' % i, '我是直推，我有：', r.json()['response'],'KSB')


