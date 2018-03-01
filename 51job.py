# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 16:38
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : 51job.py
# @Software: PyCharm
import urllib
import re

def url_input(url):
    get_html = urllib.urlopen(url)
    read_html = get_html.read().decode('gbk')
    return read_html

def find_data(html):
    #reg = re.compile(r'class="t1 ">.*?<a target="_blank" title="(.*?)"<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span><span class="t5">(.*?)</span>',re.S)
    reg = re.compile(r'class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S)
    items = re.findall(reg,html)
    return items

def find_all_page(html):
    reg = re.compile(r'.*?共(.*?)页',re.S)
    page_all = re.findall(reg, html)
    return page_all

def print_items(data_items):
    for data in data_items:
        job = data[0]
        company = data[1]
        address = data[2]
        wages = data[3]
        date = data[4]
        str = job+"--"+company+"--"+address+"--"+wages+"--"+date
        print(str)


def get_page_html(page_num):
    for i in range(page_num):
        url = "http://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=".format(i)
        print(url)

if __name__ == '__main__':
    urlstart = 'http://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    html = url_input(urlstart)
    all_page_num = find_all_page(html)
    print(all_page_num)
    data_items = find_data(html)
    print_items(data_items)