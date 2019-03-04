import redis

def get_redis():
    pool = redis.ConnectionPool(host='172.18.228.112', port=6379, password='ui375tghfsbn8')
    r = redis.Redis(connection_pool=pool)
    dl1 = '889b0e68673f47c88d0e6ca00e9a7a65' #市代    我的
    dl2 = 'a988a83e76a14cb28a0bf9dfd93d020a' #经理    黄佳强
    dl3 = 'c885e85fa40c4d2ba0feef8034c36848' #省代    顾文明
    dl4 = '81f7817729834539bfaad5cb2b77164b' #直推    客服
    dl5 = '07227eb1ae324cc49bfb705fcfb98d94' #花钱数据
    dl6 = '237448eeb0944a4eb200909949d40805'
    dl7 = '15cc42e7c5f04d51928e918f701c44de'
    dl8 = '5918455878c04277bf40a92b937f7e78'
    dl9 = 'd3ab284878964d29b144ed8b7a75de36'
    listdl = [dl1,dl2,dl3,dl4,dl5,dl6,dl7,dl8,dl9]
    for i in listdl:
        a = r.hset(name='user:UserWalletServiceImpl:userCoin', key = i, value='200000000000')   #hash用hget
        print(a)


if __name__ == '__main__':
    get_redis()