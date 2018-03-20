# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 8:51
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : xmly.py
# @Software: PyCharm
import os
import sys

import requests
from bs4 import BeautifulSoup
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}


def get_start_url():
    start_urls = ['http://www.ximalaya.com/dq/all/{}/'.format(pn) for pn in range(10)]
    for start_url in start_urls:
        response = requests.get(start_url, headers=headers).text
        soup = BeautifulSoup(response, 'lxml')
        for item in soup.find_all('div', class_='albumfaceOutter'):
            href = item.a['href']
            title = item.img['alt']
            imgurl = item.img['src']
            contxt = {
                'href': href,
                'title': title,
                'imgurl': imgurl
            }
            get_mp3(href, title)
            print('正在下载{}'.format(title))


def get_mp3(url, title):
    response = requests.get(url, headers=headers).text
    numlist = etree.HTML(response).xpath('//div[@class="personal_body"]/@sound_ids')[0].split(',')
    print(title + "存在{}".format(len(numlist)) + "个频道")
    mkdir(title)


def mkdir(title):
    path = title.strip()
    isExists = os.path.exists(os.path.join(r'D:\xmly\\', path))
    if not isExists:
        print(path)
        os.makedirs(os.path.join(r'D:\xmly\\', title))
        return True
    else:
        print("文件---" + title + "---已存在")
        return False


get_start_url()
