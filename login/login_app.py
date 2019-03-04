import redis
import time
import pymysql
import requests

url = "http://172.18.228.126:7005"

def get_uuid(mobile):
    path = 'api/v1/file/captcha/register'
    data = {"mobile": "%s" % mobile}
    api = ''.join([url, path])
    r = requests.post(url=api, data=data).json()
    z = r.get('response')
    return z

def get_pcode(uuid):
    value = "file:CaptchaServiceImpl:mobileCaptcha[%s]" % uuid  #
    pool = redis.ConnectionPool(host='172.18.228.112', port=6379, password='3nOI9ca45%$#8Gm7EH',db=10)
    r = redis.Redis(connection_pool=pool)
    p_code = r.get(value).decode('utf8')
    return p_code

def send_message(uuid, mobile, pcode):
    path = 'api/v1/user/sms/register'
    api = ''.join([url, path])
    data = {"mobile": mobile, "captcha": pcode, "uuid": uuid}
    message_code = requests.post(url=api, data=data)
    print('发送短信', message_code.text)

def get_messafe_code(mobile):
    db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_sms')
    cursor = db.cursor()
    cursor.execute('select content from send where mobile = "%s" order by id desc limit 1' % mobile)
    data = cursor.fetchone()
    string = str(data)[18:24]
    return string

def login_app(mobile, passwd):
    path = 'api/v1/user/account/login'
    api = ''.join([url, path])
    data = {"username": mobile, "password": passwd, "systemCode": 1, "loginType": 1}
    rr = requests.post(url=api, data=data).json()
    print(rr.get('response'))


def register(mobile, p_code, password):
    path = 'api/v1/user/register/mobile'
    api = ''.join([url, path])
    data2 = {"tenantCode": "gcyh", "mobile": mobile, "captcha": p_code, "password": password,
             "registerSource": "1"}
    r = requests.post(url=api, data=data2)
    print(r.text)


if __name__ == '__main__':
    passwd = '123456'
    for mobile in range(19900001111, 19900001115):
        uuid = get_uuid(mobile)
        p_code = get_pcode(uuid)
        send_message(uuid,mobile,p_code)
        safe_code = get_messafe_code(mobile)
        register(mobile, safe_code, passwd)
        login_app(mobile, passwd)
