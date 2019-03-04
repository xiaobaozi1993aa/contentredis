import pymysql
import redis
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

phone = 13066909086

def get_uuid():
    path = 'api/v1/file/captcha/register'
    url = ''.join([host, path])
    data = {"mobile": "%s" % phone}
    r = requests.post(url=url, data=data, headers=headers).json()
    print('uuid',data)
    z = r.get('response')
    y = z.get('uuid')
    return y

def password_reset():
    path = 'api/v1/user/sms/reset_password'
    url = ''.join([host, path])
    data = {"mobile":phone,"captcha":1111,"uuid":uuid}
    print(data)
    r = requests.post(url = url,data = data, headers = headers).json()
    print(r)




if __name__ == '__main__':
    get_uuid()
    uuid = get_uuid()
    password_reset()