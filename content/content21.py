import redis
import pymysql
import requests


headers = {
  "Accept": "*/*",
  "h-api-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhcGlfdXVpZCIsImgtdGVuYW50LWNvZGUiOiJnY3loIiwibG9naW5JZCI6ImFwaV91dWlkIiwiZXhwIjoxNTYyMDUwNTcyLCJpYXQiOjE1NDQ3NzA1NzE1MzN9.ig2c4If9Z0Ud4YI-V_eihzjSSvOr1eYteYUvNd0Yd28w5ZHEpTZpYQR2M-MTXCpkgu2i0GXuuoaCEuru5TSRtg",
  "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJsb2dpbklkIjoiYWRtaW5fdXVpZCIsImV4cCI6MTU2MjE1MDI1MCwiaWF0IjoxNTQ0ODcwMjQ2NTMxfQ.kMySAJzhzB-lFkhliSh2S1nYGQMaug2JIPs2ugShZU1wTTcV4n4Edb2pOHgvaRGMSe4Gj6S82BggkVYobu-j1g",
  "h-time": "1555375042088",
  "h-tenant-code": "gcyh",
  "h-nonce": "ef87a857d3324ef0b8670c2f36975284"
}

url = 'http://172.18.228.127:7005/api/v1/user/admin/invite/add_inviter?userAccountUuid=39a65170f05647bfac81dbb28a8fc07e&inviteCode='