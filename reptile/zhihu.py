import requests
from bs4 import BeautifulSoup

url = 'https://book.douban.com/subject/7067983/'

r = requests.get(url).text
#print(r)
soup = BeautifulSoup(r,'html.parser')
pinglun = soup.find_all('p','review-short hidden')
print(pinglun)

