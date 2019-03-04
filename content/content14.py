# -*- coding:utf-8 -*-




import xlrd
import json
ceshi_data = xlrd.open_workbook(r'D:\测试.xls')
sheet = ceshi_data.sheet_by_index(0)
n = sheet.nrows
m = sheet.ncols
rng = sheet.cell(0,1).value  #先行后列

print(n,m)
#print(sheet.row_values(1))
#print((sheet.col_values(1))[1])
#print(a)
#print(type(a))
#a = '{"redPacketRainUuid":"2","quantity":"2"}'
for i in range(0,n):
    b = eval((sheet.col_values(1))[i])
    print(b)
