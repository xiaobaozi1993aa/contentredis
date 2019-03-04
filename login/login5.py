import redis
import time
import pymysql
import requests

class Getcode:
    #初始化数据

    def __init__(self):

        self.headers = {
            "Accept": "*/*",
            "h-api-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhcGlfdXVpZCIsImgtdGVuYW50LWNvZGUiOiJnY3loIiwiZXhwIjoxNTUzNDc5NTAxLCJpYXQiOjE1MzYxOTk1MDE1Nzl9.TSK-6YKhnzX8ZfLN7hyjSAEiTKwHZPZAYyt0Sv6yRWlUmAMVHeYe68XRau69gDl-PlDoHNLUTvpWBeou4bY_sA",
            "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJleHAiOjE1NTM0Nzk1MDAsImlhdCI6MTUzNjE5OTQ5OTkwNn0.P42ZXPgMp8ApbDPKgYvLB-wpLFqK2XbgWbcyMEPCueRIz3FDFZwID3PXe6KHvfES0l7Wq1v45OprxcE9wpqNaw",
            "h-time": "1552356598220",
            "h-tenant-code": "gcyh",
            "h-nonce": "6917b1a82f0a43b5888af48c6a9f4100"
        }
        self.host = 'http://172.18.228.127:7005/'
    def get_phone(self):
        for i in range(19930805000, 19930805006):
            yield i

    def get_uuid(self):
        for i in self.get_phone():
            #a = self.get_phone()
            aa = str(i)
            path = 'api/v1/file/captcha/register'
            url = ''.join([self.host, path])
            data = {"mobile": "%s" % aa}
            print('号码:',aa)
            r = requests.post(url = url,data = data, headers = self.headers).json()
            z = r.get('response')
            yield z

    def get_pcode(self):
        for i in self.get_uuid():
            y = i.get('uuid')
            value = "file:CaptchaServiceImpl:mobileCaptcha[%s]" % y  #
            pool = redis.ConnectionPool(host='120.78.201.240', port=6379, password='2018375tghfsbn8')
            r = redis.Redis(connection_pool=pool)
            p_code = r.get(value).decode('utf8')
            yield p_code

    def send_message(self):
        for i in self.get_uuid():
            y = i.get('uuid')
            path1 = 'api/v1/user/sms/register'
            url1 = ''.join([self.host, path1])
            data1 = {"mobile": a, "captcha": b, "uuid": y}
            print(data1)
            message_code = requests.post(url=url1, data=data1, headers=self.headers)
            print('发送短信', message_code.text)

    def get_messafe_code(self):
        for i in self.get_phone():
            db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_sms')
            cursor = db.cursor()
            cursor.execute('select content from send where mobile = "%s" order by id desc limit 1' % i)
            data = cursor.fetchone()
            print(data)
            string = str(data)[18:24]
aa = Getcode()
aa.get_pcode()