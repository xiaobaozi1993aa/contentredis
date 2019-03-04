import requests
import pymysql
import redis
import time

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
    #注册手机号类型
    def zdyphone(self):
        data = ['19930807047','19930807048','19930807049','19930807050','19930807051','19930807052','19930807053']
        for phone in data:
            return phone
    #获取uuid接口
    def get_uuid(self, phone):
        path = 'api/v1/file/captcha/register'
        url = ''.join([self.host, path])
        data = {"mobile": "%s" % phone}
        r = requests.post(url = url,data = data, headers = self.headers).json()
        z = r.get('response')
        y = z.get('uuid')
        print(y)
        return y
    #连接redis，获取图形验证码
    def get_picture_code(self,uuid):
        value = "file:CaptchaServiceImpl:mobileCaptcha[%s]" % uuid#
        pool = redis.ConnectionPool(host='120.78.201.240', port=6379, password='2018375tghfsbn8')
        r = redis.Redis(connection_pool=pool)
        b = r.get(value).decode('utf8')
        print(b)
        return b
    #发送短信验证码
    def get_message_code(self, uuid, p_code, phone):
        path1 = 'api/v1/user/sms/register'
        url1 = ''.join([self.host, path1])
        data1 = {"mobile": phone, "captcha": p_code, "uuid": uuid}
        print(data1)
        message_code = requests.post(url=url1, data=data1, headers=self.headers)
        return message_code
    #数据库获取短信验证码
    def get_mysql_code(self, phone):
        db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_sms')
        cursor = db.cursor()
        cursor.execute('select content from send where mobile = "%s" order by id desc limit 1' % phone)
        data = cursor.fetchone()
        string = str(data)[15:21]
        return string

#phone = '19930808015'
password = '123456'
test = Getcode()
phone = test.zdyphone()
print(phone)
uuid = test.get_uuid(phone)                      #调用get_uuid返回的uuid，并赋值
p_code = test.get_picture_code(uuid)                #调用redis获取图形验证码字符串
a = test.get_message_code(uuid,p_code,phone)
print('发送短信验证码',a.json())
b = test.get_mysql_code(phone)
print('获取短信验证码',b)
time.sleep(1)

class Register(Getcode):
    # 注册成功
    def register(self,message_code):
        path = 'api/v1/user/register/mobile'
        url = ''.join([self.host,path])
        data = {"tenantCode":"gcyh","mobile":phone,"captcha":message_code,"password":password,"registerSource":"1"}
        print('注册数据:',data)
        r = requests.post(url = url,data = data,headers = self.headers)
        print('注册接口返回:',r.text)
        print(r.status_code)
        return r
    #登录成功
    def login(self,phone,password):
        path = 'api/v1/user/account/login'
        url = ''.join([self.host,path])
        data = {"username":phone,"password":password,"systemCode":1,"loginType":1}
        print('登录数据:',data)
        r = requests.post(url = url,data = data,headers = self.headers).json()
        print('登录数据返回:',r)



c = Register()
c.register(b)
c.login(phone,password)

