import requests
import redis
import datetime
import pymysql


class Register:
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
        #self.phone = '19930808102'

    # 获取uuid放入redis
    def get_uuid(self, phone):
        #nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 时间字符串
        path = 'api/v1/file/captcha/register'
        url = ''.join([self.host, path])
        data = {"mobile": "%s" % phone}
        r = requests.post(url = url,data = data, headers = self.headers).json()
        z = r.get('response')
        y = z.get('uuid')
        return y

    #连接redis，获取图形验证码
    def get_picture_code(self,uuid):
        value = "file:CaptchaServiceImpl:mobileCaptcha[%s]" % uuid#
        pool = redis.ConnectionPool(host='120.78.201.240', port=6379, password='ui375tghfsbn8')
        r = redis.Redis(connection_pool=pool)
        b = r.get(value).decode('utf8')
        return b

    #发送短信验证码
    def get_message_code(self, uuid, p_code, phone):
        path1 = 'api/v1/user/sms/register'
        url1 = ''.join([self.host, path1])
        data1 = {"mobile": "%s" % phone, "captcha": p_code, "uuid": uuid}
        print(data1)
        message_code = requests.post(url=url1, data=data1, headers=self.headers)
        #print(message_code.text)
        return message_code
    #数据库获取短信验证码
    def get_mysql_code(self, phone):
        db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_sms')
        cursor = db.cursor()
        cursor.execute('select content from send where mobile = "%s" order by id desc limit 1' % phone)
        data = cursor.fetchone()
        string = str(data)[15:21]
        #print(string)
        return string
    #注册成功
    def register(self,message_code, **kwargs):
        path = 'api/v1/user/register/mobile'
        url = ''.join([self.host,path])
        #data = {"tenantCode":"gcyh","mobile":"%s" % self.phone,"captcha":message_code,"password":"199308","registerSource":"1"}
        #print(type(data))
        #for kv in data.items():
            #print(type(kv))
        r = requests.post(url = url,data = kwargs,headers = self.headers)
        print(r.text)
        return r

def BaseTest(phone, **kwargs):
    #phone = '19930808102'
    test = Register()
    uuid = test.get_uuid(phone)                      #调用get_uuid返回的uuid，并赋值
    p_code = test.get_picture_code(uuid)
    message_code = test.get_mysql_code(phone)
    #data = {"tenantCode":"gcyh","mobile":phone,"captcha":message_code,"password":"199308","registerSource":"1"}
    print(test.get_message_code(uuid, p_code, phone))
    print(test.get_mysql_code(phone))
    print(test.register(message_code,kwargs))

def test1():
    get_value()
    BaseTest()

def test2():
    get_value()
    BaseTest()

