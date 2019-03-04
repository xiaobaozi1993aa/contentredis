import redis
import pymysql
import requests

#phone_data = ['19930807047', '19930807048', '19930807049', '19930807050', '19930807051', '19930807052', '19930807053']


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
    #获取uuid接口
    def get_uuid(self):
        for b in range(19930808100,19930808200):
            a = str(b)
            path = 'api/v1/file/captcha/register'
            url = ''.join([self.host, path])
            data = {"mobile": "%s" % a}
            print('号码:',a)
            r = requests.post(url = url,data = data, headers = self.headers).json()
            z = r.get('response')
            y = z.get('uuid')
            value = "file:CaptchaServiceImpl:mobileCaptcha[%s]" % y#
            print(value)
            pool = redis.ConnectionPool(host='120.78.201.240', port=6379, password='2018375tghfsbn8',db=10)
            r = redis.Redis(connection_pool=pool)
            b = r.get(value).decode('utf8')
            print('获取图形验证码:', b)
            path1 = 'api/v1/user/sms/register'
            url1 = ''.join([self.host, path1])
            data1 = {"mobile": a, "captcha": b, "uuid": y}
            print(data1)
            message_code = requests.post(url=url1, data=data1, headers=self.headers)
            print('发送短信',message_code.text)
            db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_sms')
            cursor = db.cursor()
            cursor.execute('select content from send where mobile = "%s" order by id desc limit 1' % a)
            data = cursor.fetchone()
            print(data)
            string = str(data)[18:24]
            path = 'api/v1/user/register/mobile'
            url = ''.join([self.host, path])
            data2 = {"tenantCode": "gcyh", "mobile": a, "captcha": string, "password": 123456,
                    "registerSource": "1"}
            print(data2)
            r = requests.post(url=url, data=data2, headers=self.headers)
            print('注册接口返回:', r.text)
            path = 'api/v1/user/account/login'
            url = ''.join([self.host, path])
            data = {"username": a, "password": 123456, "systemCode": 1, "loginType": 1}
            rr = requests.post(url=url, data=data, headers=self.headers).json()
            print(rr.get('response'))





aa = Getcode()
aa.get_uuid()


