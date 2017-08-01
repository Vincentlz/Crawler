# -*- coding: utf-8 -*-
''' ---------------------------------------
   程序：CrawlerDBmz1.py
   版本：1.0
   作者：vincentlz
   日期：2017/8/1 15:07
   语言：Python 3.6
   工具：PyCharm
   简介：下载指定网站上的妹子图片，这里只抓了前100页的图片，可根据需要自己设置页数
        cat值为图片类型，大家可以自行更改cat值体验一下，有问题留言给我，看到就会解答
        2 ＝ 大胸妹
        3 ＝ 美腿控
        4 ＝ 有颜值
        5 ＝ 大杂烩
        6 ＝ 小翘臀
  ---------------------------------------'''

import requests
import re
import time
from bs4 import BeautifulSoup

cat ='2'
img = 'http://www.dbmeinv.com/dbgroup/show.htm?cid='+ cat
end = '/dbgroup/show.htm?cid='+ cat + '&pager_offset=3'
urls = [ ]
def getURLs(mainURL):
    time.sleep(1)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    html = requests.get(mainURL).text
    soup = BeautifulSoup(html, 'html.parser')
    picURL = re.findall('<img class.*?src="(.+?\.jpg)"', html, re.S)
    for url in picURL:
        urls.append(url)
        print(url)
    asoup = soup.select('.next a')[0]['href']
    Next_page = 'http://www.dbmeinv.com' + asoup
    if asoup != end:
        getURLs(Next_page)
    else:
        print('链接已处理完毕！')
    return urls
url = getURLs(img)

i = 0
for each in url:
    pic = requests.get(each, timeout = 10)
    picName = 'E:/Code/patu/pictures/' + str(i) + '.jpg'
    fp = open(picName, 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1

print('图片下载完成')