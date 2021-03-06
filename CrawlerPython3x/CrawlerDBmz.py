# -*- coding: utf-8 -*-
''' ---------------------------------------
   程序：CrawlerDBmz.py
   版本：1.0
   作者：vincentlz
   日期：2017/8/1 14:52
   语言：Python 3.6
   工具：PyCharm
   简介：爬取豆瓣妹子图
  ---------------------------------------'''

import urllib.request
import os
import re
import time
from bs4 import BeautifulSoup

webheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

img_index = 1


def processDouban(page_url):
    list_url = page_url

    # print(all_data)


if __name__ == '__main__':
    pageIndex = 2525
    index = 1
    os.mkdir('doubanimages')
    while pageIndex > 0:
        pageUrl = 'http://www.dbmeinv.com/?pager_offset=' + str(pageIndex)
        try:
            list_req = urllib.request.Request(url=pageUrl, headers=webheader)
            list_Page = urllib.request.urlopen(list_req)
            all_data = list_Page.read().decode('utf-8')
            current_soup = BeautifulSoup(all_data, 'html.parser')
            current_list = current_soup.find_all('img', {'class': 'height_min'})
            for list in current_list:
                # print(list['href'])
                time.sleep(1)
                print(time.strftime("%H:%M:%S     ") + '处理图片: ' + list['src'])
                try:
                    file = open('doubanimages//' + str(index) + '.jpg', "wb")
                    req = urllib.request.Request(list['src'], headers=webheader)

                    webPage = urllib.request.urlopen(req)
                    data = webPage.read()
                    file.write(data)
                except:
                    print('打开图片失败')
                    file.flush()
                    file.close()
                    index += 1
                    # img_index += 1
                else:
                    file.flush()
                    file.close()
                    index += 1
        except:
            pageIndex -= 1
        else:
            pageIndex -= 1