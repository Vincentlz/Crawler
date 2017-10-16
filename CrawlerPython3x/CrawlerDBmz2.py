# -*- coding: utf-8 -*-
''' ---------------------------------------
   程序：CrawlerDBmz2.py
   版本：1.0
   作者：vincentlz
   日期：2017/8/1 15:12
   语言：Python 3.6
   工具：PyCharm
   简介：选择输入下载图片 http://whjgithub.github.io/2014/11/08/2014-11-08-210858/
   1.运行失败需要研究一下（学习思路）
   2.已修改运行成功可以进行选择下载，目前图片下载不全，需进一步研究
  ---------------------------------------'''

import os
import urllib.request
import re

info = u'''
---------------------------
1.所有()
2.大胸妹
3.美腿控
4.有颜值
5.大杂烩
6.黑丝袜
7.小翘臀
请输入数字选择要下载的类别:
---------------------------
'''
print(info)
num = input()  # 获取下载选项
choices = {
    '1': r'',
    '2': r'2',
    '3': r'3',
    '4': r'4',
    '5': r'5',
    '6': r'6',
    '7': r'7'
}
choice = 'cid='+choices[num]
# choice = choices[num] #所有
base_url = r'http://www.dbmeinv.com/dbgroup/show.htm?'
choice_url = base_url + choice  # 要下载的页面的首页url
print(u'请输入起始页数：')
startpage = input()
print(u'请输入结束页数：')
endpage = input()
page_index = r'&pager_offset='
url_pages = []  # 储存所有要下载的url
# 拼接url的各个部分
for index in range(int(startpage), int(endpage) +1):
    url_pages.append(choice_url + page_index + str(index))
print(url_pages)
print(u'请输入要保存图片的绝对路径：')
dir_path = input()  # 保存路径名
print(u'请输入要保存图片的文件夹名称：')
dir_title = input()  # 保存文件夹名
new_path = os.path.join(dir_path, dir_title)  # 拼接出最终的路径
if not os.path.isdir(new_path):  # 如果不存在就创建文件夹
    os.makedirs(new_path)
    print(u'将把图片保存在：%s' % new_path)
j = int(startpage)  # 用来给图片编号
for page in url_pages:  # 循环每个要下载的页面
    myUrl = page  # 取出一个url
    content = urllib.request.urlopen(myUrl).read().decode('utf-8')  # 获取url的html代码
    pattern = re.compile(r'<img.*?class=".*?_min".*?src="(.*?)".*?alt=.*?>' \
                         , re.S)  # 正则表达式对象
    allurl = re.findall(pattern, content)  # 找到并返回所有符合对象的值，即图片链接
    # i = 0  # 编号用
    for item in allurl:
        location = r'%s\%s.jpg' % (new_path, j)  # 图片存储路径
        urllib.request.urlretrieve(item, location)  # 下载图片到指定位置
        # i += 1
    j += 1
