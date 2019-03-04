import requests
import pymysql

mobile = (x+1 for x in range(19930808000,19930808005))
host = 'http://172.18.228.127:7005/'


headers = {
            "Accept": "*/*",
            "h-api-token": "eyJhbGciOiJIUzUxMiJ9.eyJtb2JpbGUiOiIxOTkzMDgwNTAwNSIsInN1YiI6IjZkZmY4OWE0OGM0ODRlZjZhNWJhNDc5Nzc5OWYyMjUyIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJsb2dpbklkIjoiYTQwNjA4MmQ0YmU2NGYwMDljYjExOWIxNWZjMTE1NmUiLCJleHAiOjE1NjM3MDY2ODMsImlhdCI6MTU0NjQyNjY4MzYwOH0.RYh3QI9HPiO--fmxUTAB8uevMmBs2v1f1OnLcPWkDmCZDpfsNmtvVhkC18UhNjUiFhMQMOQX3OGJbW55I8p88A",
            "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJleHAiOjE1NTM0Nzk1MDAsImlhdCI6MTUzNjE5OTQ5OTkwNn0.P42ZXPgMp8ApbDPKgYvLB-wpLFqK2XbgWbcyMEPCueRIz3FDFZwID3PXe6KHvfES0l7Wq1v45OprxcE9wpqNaw",
            "h-time": "1552356598220",
            "h-tenant-code": "gcyh",
            "h-nonce": "6917b1a82f0a43b5888af48c6a9f4100"
        }
def get_response():
    url = 'http://172.18.228.127:7005/api/v1/activity/beehiveActivity/info'
    r = requests.get(url=url,headers=headers).json()
    print(r)

if __name__ == '__main__':
    get_response()
