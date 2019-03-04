# -*- coding:utf-8 -*-

'''
@versoin:1.0
@author:t-bag
@file:content12.py
@time:2018-12-5 19:12:55
'''
from ddt import ddt,data,file_data,unpack
import unittest
import requests
import xlrd
import json
#打开Excel文件
ceshi_data = xlrd.open_workbook(r'D:\测试.xls')
#打开第一张sheet表
sheet = ceshi_data.sheet_by_index(0)
#取某一个单元格的值，json.loads把字符串转为字典格式
#ac,b = json.loads(sheet.cell(1,1).value),json.loads(sheet.cell(0,1).value)
#取第一列的值，eval把字符串转为字典格式
a = [eval((sheet.col_values(1))[i]) for i in range(0,3)]
#print(a)
b = [sheet.col_values(0)[i] for i in range(0,3)]
#print(b)
path = '/api/v1/redpacket/red_packet_rain/draw'
@ddt #类调用ddt函数解释器
class ceshi(unittest.TestCase):
    def setUp(self):        #setup初始化
        self.headers = {
          "Accept": "*/*",
          "h-api-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhcGlfdXVpZCIsImgtdGVuYW50LWNvZGUiOiJnY3loIiwiZXhwIjoxNTUzNDc5NTAxLCJpYXQiOjE1MzYxOTk1MDE1Nzl9.TSK-6YKhnzX8ZfLN7hyjSAEiTKwHZPZAYyt0Sv6yRWlUmAMVHeYe68XRau69gDl-PlDoHNLUTvpWBeou4bY_sA",
          "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJleHAiOjE1NTM0Nzk1MDAsImlhdCI6MTUzNjE5OTQ5OTkwNn0.P42ZXPgMp8ApbDPKgYvLB-wpLFqK2XbgWbcyMEPCueRIz3FDFZwID3PXe6KHvfES0l7Wq1v45OprxcE9wpqNaw",
          "h-time": "1553890943938",
          "h-tenant-code": "gcyh",
          "h-nonce": "5959977aae7a474ab0340a28ad3e3515"
        }
        self.host = 'http://172.18.228.127:7005/'

    @data(*a)       #方法调用data，多个值前加*
    def test1(self,value):

        url = ''.join([self.host, path])
        r = requests.post(url,data = value,headers = self.headers)
        assert r.status_code == 200
        assert r.json()['message'] in ('红包雨存在','断言还失败')

if __name__ == '__main__':
    unittest.main(verbosity=6)