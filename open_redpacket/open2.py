import redis
import pymysql

a = ['45f7eb65840f417fb138d3277d0ef8f7', '235bf16caa1144f88f9bfda1fff10463', '82603af59fc74caa8a5812ad58c1eeee',
     '5db6ce93f7ae4c1bb8fa8ed2540d98d2', '99d234981c024d1b8cd6c36c9cc9f62b','66f01f61006b4982afab6dbf98981a19']


def sql_update():
    for b in a:
        db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_user')
        cursor = db.cursor()
        cursor.execute("update user_wallet set coin = 0 where user_account_uuid = '%s'"% b)
        db.commit()
        cursor.close()
def hash_update():
    pool = redis.ConnectionPool(host='172.18.228.112', port=6379, password='2018375tghfsbn8',db=10)
    r = redis.Redis(connection_pool=pool)
    for y in a:
        b = r.hset(name='user:UserWalletServiceImpl:userCoin',key='%s' %y,value=0)
        print(b)

if __name__ == '__main__':
    sql_update()
    hash_update()
