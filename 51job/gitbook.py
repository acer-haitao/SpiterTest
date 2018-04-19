# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 8:59
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : gitbook.py
# @Software: PyCharm
import urllib


def url_input(url):
    """
    获取网页源码html信息
    """
    try:
        get_html = urllib.urlopen(url)
        read_html = get_html.read().decode('utf8')
    except Exception as e:
        print(e)
        read_html = None
    return read_html


url = 'https://legacy.gitbook.com/@wizardforcel'
html = url_input(url)
print(html)
