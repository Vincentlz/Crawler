# -*- coding: utf-8 -*-
''' ---------------------------------------
   程序：CrawlerDBmz3.py
   版本：1.0
   作者：vincentlz
   日期：2017/8/1 15:24
   语言：Python 3.6
   工具：PyCharm
   简介：有问题，可能需要加个请求头伪装
  ---------------------------------------'''

import sys, urllib.request, re, time

global num
num = 0
i = 0


def getURL(n):
    url = urllib.request.urlopen('http://www.dbmeizi.com/category/14?p=%d' % n)
    data = url.read()
    r = re.compile(r'http://pic.dbmeizi.com/npics/[a-z0-9-]{3}/[a-z0-9-]{3}/s_p[0-9]{8}.jpg')
    pic = r.findall(data)
    return pic


for page in range(1, 10):
    girl = getURL(page)
    length = len(girl)
    for i in range(0, length):
        url2 = urllib.request.urlopen(girl[i])
        data2 = url2.read()
        f = open('E:/Code/patu/%d.jpg' % num, 'wb')
        f.write(data2)
        f.close()
        print(num)
        num = num + 1
        time.sleep(1)
print('结束')
