import xlrd


path = 'D:/接口测试用例.xls'

testcase = xlrd.open_workbook(path)   #打开Excel

sheet =testcase.sheet_by_index(0)       #打开sheet

print(sheet.cell(1,1).value)            #前面是横（数字），后面是竖（字母）
print(sheet.cell(1,2).value)
print(sheet.ncols)              #获取列数，就是字母那行

print(sheet.nrows)              #获取行数，就是数字那行

