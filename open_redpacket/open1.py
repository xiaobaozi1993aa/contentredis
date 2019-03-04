import redis
import pymysql
import requests

host = 'http://test_gateway.guochuangyuanhe.com/'
sum = 0
for i in range(19930808100,19930808110):
    a = str(i)
    path = 'api/v1/user/account/login'
    url = ''.join([host, path])
    data = {"username": a, "password": 123456, "systemCode": 1, "loginType": 1}
    r = requests.post(url=url, data=data).json()
    token = r.get('response')
    print(token)
    headers1 = {
        "Accept": "*/*",
        "h-api-token": token,
        "h-time": "1555554375874",
        "h-tenant-code": "gcyh",
        "h-nonce": "6a669a27a7f04ee0a9df70206195de52"
    }
    open_path = 'https://test_gateway.guochuangyuanhe.com/api/v1/redpacket/red_packet_pool/open'
    open_data = {"latitude": 22.630186, "longitude": 113.822961, "redPacketUuid": "ae90a2d2694748e59b5c9257a9a4f1e3"}
    rr = requests.post(url=open_path, data=open_data, headers=headers1).json()
    #money = ((rr.get('response').get('coin')))
    #aaa = float(money)
    #sum += aaa
    #print('KSB金额',sum)
    print(rr)