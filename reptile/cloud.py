import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/subject/27110296/'

r = requests.get(url = url).text
#r.encoding = 'utf-8'
soup = BeautifulSoup(r,'html.parser')

#a = soup.find_all('a','name')
b = soup.find_all('div','main review-item')
#print(b)
for n in (b):
    name = n.get_text(r.xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/a/text()'.format(i)))
    message = n.get_text('p')
    data = {name:message}
    print(name)


