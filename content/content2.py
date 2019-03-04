import requests
import re
import redis
import pymysql

headers = {
  "Accept": "*/*",
  "h-api-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhcGlfdXVpZCIsImgtdGVuYW50LWNvZGUiOiJnY3loIiwiZXhwIjoxNTUzNDc5NTAxLCJpYXQiOjE1MzYxOTk1MDE1Nzl9.TSK-6YKhnzX8ZfLN7hyjSAEiTKwHZPZAYyt0Sv6yRWlUmAMVHeYe68XRau69gDl-PlDoHNLUTvpWBeou4bY_sA",
  "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJleHAiOjE1NTM0Nzk1MDAsImlhdCI6MTUzNjE5OTQ5OTkwNn0.P42ZXPgMp8ApbDPKgYvLB-wpLFqK2XbgWbcyMEPCueRIz3FDFZwID3PXe6KHvfES0l7Wq1v45OprxcE9wpqNaw",
  "h-time": "1552356598220",
  "h-tenant-code": "gcyh",
  "h-nonce": "6917b1a82f0a43b5888af48c6a9f4100"
}
#图形验证码uuid获取
phone = '1993080860'
path = 'api/v1/file/captcha/register'
host = 'http://172.18.228.127:7005/'
url = ''.join([host,path])
data = {"mobile": "%s" % phone}
r = requests.post(url = url,data = data, headers = headers).json()
print(r)
print(type(r))
z = r.get('response')
print(z)
y = z.get('uuid')
print(y)
print(type(y))
#把uuid赋值到redisget请求中，获取图形验证码
value = "file:CaptchaServiceImpl:mobileCaptcha[%s]" % y
pool = redis.ConnectionPool(host = '120.78.201.240',port=6379,password = 'ui375tghfsbn8')
print(value)
r = redis.Redis(connection_pool=pool)
b = r.get(value).decode('utf8')
print(b)
#获取短信验证码
path1 = 'api/v1/user/sms/register'
url1 = ''.join([host,path1])
data1 = {"mobile": "%s" % phone,"captcha":"%s" % b,"uuid":"%s" % y}
print(data1)
message_code = requests.post(url = url1,data = data1,headers = headers)
print(message_code.text)
#数据库查询验证码
db = pymysql.Connect('172.18.228.112','root','3nOI9ca45%$#8Gm7EH','gcyh_sms')
cursor = db.cursor()
cursor.execute('select content from send where mobile = "%s" order by id desc limit 1' % phone)
data = cursor.fetchone()
print(data)
string = str(data)[15:21]
print(string)