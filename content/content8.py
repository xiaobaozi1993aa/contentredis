import requests
import pymysql
import redis

#数据库连接查询获取数据
def get_mysql():
    #打开数据库连接
    db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_sms')
    #使用cursor()方法创建一个游标对象
    cursor = db.cursor()
    #使用execute()方法执行SQL查询
    cursor.execute('select content from send where mobile = "13048818475"')
    #使用fetchone()方法获取单条数据
    data = cursor.fetchone()
    #字符串截取，获取想要的数据
    string = str(data)[15:21]
    print(string)

#Redis连接查询获取数据
'''def get_redis():
    #打开redis连接
    pool = redis.ConnectionPool(host='120.78.201.240', port=6379, password='ui375tghfsbn8')
    #get方法输入键值对获取输出
    r = redis.Redis(connection_pool=pool)
    # % y 字符串格式化重新赋值
    value = "file:CaptchaServiceImpl:mobileCaptcha[%s]" % y
    b = r.get(value).decode('utf8')
    print(b)
'''
if __name__ == '__main__':
    get_mysql()


