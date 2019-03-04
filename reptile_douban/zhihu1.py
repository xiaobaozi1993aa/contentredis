import requests
from bs4 import BeautifulSoup
import re

def get_movie():
    url = 'https://movie.douban.com/subject/27110296/reviews'
    r = requests.get(url).text
    soup = BeautifulSoup(r,'html.parser')
    pinglun = soup.find_all('p')
    name = soup.find_all('a',class_= 'name')
    print(pinglun)
    for i in name:
        douban_name = i.text
        #print(douban_name)
        return douban_name
    for i in pinglun:
        douban_content = i.text
        print(douban_content)
        return douban_content
if __name__ == '__main__':
    get_movie()

    