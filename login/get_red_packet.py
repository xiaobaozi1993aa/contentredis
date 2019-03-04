import requests
host = 'http://172.18.228.127:7005/'
headers = {
            "Accept": "*/*",
            "h-api-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhcGlfdXVpZCIsImgtdGVuYW50LWNvZGUiOiJnY3loIiwiZXhwIjoxNTUzNDc5NTAxLCJpYXQiOjE1MzYxOTk1MDE1Nzl9.TSK-6YKhnzX8ZfLN7hyjSAEiTKwHZPZAYyt0Sv6yRWlUmAMVHeYe68XRau69gDl-PlDoHNLUTvpWBeou4bY_sA",
            "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJleHAiOjE1NTM0Nzk1MDAsImlhdCI6MTUzNjE5OTQ5OTkwNn0.P42ZXPgMp8ApbDPKgYvLB-wpLFqK2XbgWbcyMEPCueRIz3FDFZwID3PXe6KHvfES0l7Wq1v45OprxcE9wpqNaw",
            "h-time": "1552356598220",
            "h-tenant-code": "gcyh",
            "h-nonce": "6917b1a82f0a43b5888af48c6a9f4100"
        }
for i in range(19930808000,19930808010):
    path = 'api/v1/user/account/login'
    url = ''.join([host, path])
    data = {"username": i, "password": 123456, "systemCode": 1, "loginType": 1}
    rr = requests.post(url=url, data=data, headers=headers).json()
    #print('登录数据返回:',i, rr)
    token1 = rr['response']
    headers1 = {
        "Accept": "*/*",
        "h-api-token":"eyJhbGciOiJIUzUxMiJ9.eyJtb2JpbGUiOiIxOTkzMDgwODAyMCIsInN1YiI6IjljMTcyYWJiZWJlZTQwODg5Yjc2NDcxM2YzMjIxY2Q5IiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJsb2dpbklkIjoiYWQ5ZjE0MjFlYjI0NDM3OTlkZDVkZWJjYTNhNDAyM2QiLCJleHAiOjE1NjM1NTgyMjcsImlhdCI6MTU0NjI3ODIyNzM0M30.mAIwIEV30S7s8Fc929vXup_7b9cflOGCzX6-CtwRnzYFoQhPOcyRLASWi57Gzf9NhO7QaGrPbi3DqzGZLCXshQ",
        "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJleHAiOjE1NTM0Nzk1MDAsImlhdCI6MTUzNjE5OTQ5OTkwNn0.P42ZXPgMp8ApbDPKgYvLB-wpLFqK2XbgWbcyMEPCueRIz3FDFZwID3PXe6KHvfES0l7Wq1v45OprxcE9wpqNaw",
        "h-time": "1552356598220",
        "h-tenant-code": "gcyh",
        "h-nonce": "6917b1a82f0a43b5888af48c6a9f4100"
    }
    #path1 = '/api/v1/redpacket/red_packet_pool/open'
    #url1 = ''.join([host, path1])
    #data1 = {"longitude":"113.822963","latitude":"22.630187","redPacketUuid":"31eb4a4589e249f18527b36eaf187d2c"}
    #rrr = requests.post(url=url1, data=data1, headers=headers).json()
    #print('抢红包数据返回:',i, rrr)

    path2 = '/api/v1/redpacket/person_red_packet/open'
    url1 = ''.join([host, path2])
    data1 = {"redPacketUuid": "78abbb9f4f234af59959938e25b45cdc"}
    r = requests.post(url=url1, data=data1, headers=headers1).json()
    print('摇一摇数据返回:',r)