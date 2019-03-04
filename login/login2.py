import redis
import pymysql
import requests

class Safecode:

    def __init__(self):

        self.headers = {
              "Accept": "*/*",
              "h-api-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhcGlfdXVpZCIsImgtdGVuYW50LWNvZGUiOiJnY3loIiwibG9naW5JZCI6ImFwaV91dWlkIiwiZXhwIjoxNTYyMDUwNTcyLCJpYXQiOjE1NDQ3NzA1NzE1MzN9.ig2c4If9Z0Ud4YI-V_eihzjSSvOr1eYteYUvNd0Yd28w5ZHEpTZpYQR2M-MTXCpkgu2i0GXuuoaCEuru5TSRtg",
              "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJsb2dpbklkIjoiYWRtaW5fdXVpZCIsImV4cCI6MTU2MjE1MDI1MCwiaWF0IjoxNTQ0ODcwMjQ2NTMxfQ.kMySAJzhzB-lFkhliSh2S1nYGQMaug2JIPs2ugShZU1wTTcV4n4Edb2pOHgvaRGMSe4Gj6S82BggkVYobu-j1g",
              "h-time": "1555554375874",
              "h-tenant-code": "gcyh",
              "h-nonce": "6a669a27a7f04ee0a9df70206195de52"
            }
        self.host = 'http://test_gateway.guochuangyuanhe.com/'

    def get_uuid(self):
        for b in range(19931993000,19931993100):
            a = str(b)
            path = 'api/v1/file/captcha/reset_safe_code?mobile= %s' % a
            url = ''.join([self.host, path])
            r = requests.post(url=url,headers=self.headers).json()
            print(r.json())
            aa = r['response']
            uuid = aa['uuid']
            value = "file:CaptchaServiceImpl:mobileCaptcha[%s]" % uuid  #
            pool = redis.ConnectionPool(host='120.78.201.240', port=6379, password='2018375tghfsbn8',db=10)
            r = redis.Redis(connection_pool=pool)
            b = r.get(value).decode('utf8')
            #print('获取图形验证码',b)
            path1 = '/api/v1/user/sms/reset_safety_code'
            data = {'mobile':a,'captcha':b,'uuid':uuid}
            url1 = ''.join([self.host, path1])
            r1 = requests.post(url=url1,data=data,headers=self.headers ).json()
            print('发送短信',r1)
            db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_sms')
            cursor = db.cursor()
            cursor.execute('select content from send where mobile = "%s" order by id desc limit 1' % a)
            data1 = cursor.fetchone()
            print(data1)
            string = str(data1)[22:28]
            print('短信验证码提取',string)
            path4 = 'api/v1/user/account/login'
            url6 = ''.join([self.host, path4])
            data4 = {"username": a, "password": 123456, "systemCode": 1, "loginType": 0}
            #print('登录数据:', data4)
            r6 = requests.post(url=url6, data=data4, headers=self.headers).json()
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
            path2 = '/api/v1/user/safe/reset'
            data2 = {'captcha':string,'safetyCode':199308}
            url2 = ''.join([self.host, path2])
            r2 = requests.post(url=url2,data=data2,headers=headers1).json()
            print(a,'绑定交易密码',r2)

a = Safecode()
a.get_uuid()