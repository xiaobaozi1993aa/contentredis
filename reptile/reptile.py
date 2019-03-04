import requests
import xml
from bs4 import BeautifulSoup
from lxml import html

url = 'https://sj.qq.com/myapp/detail.htm?apkName=com.sz.gcyh.KSHongBao'
f = requests.get(url).text
#print(f)
soup = BeautifulSoup(f,'html.parser')

all_text = soup.find_all('div','r')
print(all_text)


