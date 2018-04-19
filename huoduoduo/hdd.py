# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 8:51
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : hdd.py
# @Software: PyCharm
from selenium import webdriver

url = "https://weidian.com/index.html?userid=845925946"
driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
driver.get(url)
print (driver.page_source)
