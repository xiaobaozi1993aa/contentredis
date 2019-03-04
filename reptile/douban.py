import requests
from lxml import etree
from tqdm import tqdm
import time
import random
import pandas as pd

name_list, content_list = [], []


def get_content(page):
    url = "https://movie.douban.com/subject/26752088/comments?start=20&limit=20&sort=new_score&status=P&percent_type={}" \
        .format(page * 20)
    res = requests.get(url)
    res.encoding = "utf-8"
    if (res.status_code == 200):
        print("\n第{}页短评爬取成功！".format(page + 1))
    else:
        print("\n第{}页爬取失败！".format(page + 1))

    x = etree.HTML(res.text)
    for i in range(1, 21):
        name = x.xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/a/text()'.format(i))
        content = x.xpath('//*[@id="comments"]/div[{}]/div[2]/p/text()'.format(i))
        name_list.append(name[0])
        content_list.append(str(content[0]).strip())


if __name__ == '__main__':
    for i in tqdm(range(0, 10)):
        get_content(i)
        time.sleep(random.randrange(6, 9))
    infos = {'name': name_list, 'content': content_list}
    data = pd.DataFrame(infos, columns=['name', 'content'])
    data.to_csv("豆瓣《我不是药神》.csv")
