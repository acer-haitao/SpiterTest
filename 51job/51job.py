# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 16:38
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : 51job.py
# @Software: PyCharm
import re
import sqlite3
import sys
import urllib

from jobnameconfig import jobname, urlstart
from urlconfig import urldict

reload(sys)
sys.setdefaultencoding('utf8')#处理打印中文字体用Unicode编码

i = 0#统计爬取总条目
def url_input(url):
    """
    获取网页源码html信息
    """
    get_html = urllib.urlopen(url)
    read_html = get_html.read().decode('gbk')
    return read_html

def find_data(html):
    """
    用正则表达式获取需要的信息
    """
    reg = re.compile(r'class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S)
    items = re.findall(reg,html)
    return items

def find_all_page(html):
    """
    从第一页中获取总页数
    """
    reg = re.compile(r'<span class="td">(.*?)</span><input id="jump_page" class="mytxt" type="text" value="1"/>',re.S)
    page_all = re.findall(reg, html)
    num = re.sub("\D", "", page_all[0])#从共5页中提取数字
    return num

def data_to_sqlite(id,job,company,address,wages,date,jobname):
    """
    将信息存储到数据库
    """
    db = sqlite3.connect("D:\Python-Test\WeiXin\db.sqlite3")
    cursor = db.cursor()  # OR IGNORE重复数据会跳过
    sql = "insert  OR IGNORE into '51jobtest'(job,company,address,wages,date,jobname) values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % (
    job, company, address, wages, date, jobname)
    # sql = "insert OR IGNORE  into '51jobtest'(job,company,address,wages,date,jobname) values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % ("job", "company", "address", "wages", "date", "jobname")
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("SQLERRO:",e)

def data_to_txt(str,jobname):
    """
    将信息存储到文本
    """
    with open(u"51job%s.txt"%(jobname),'a+') as f:
        f.write(str)

def print_items(data_items,jobname):
    """
    从正则匹配后的列表中获取信息存储打印
    """
    global i
    for data in data_items:
        job = data[0]
        company = data[1]
        address = data[2]
        wages = data[3]
        date = data[4]
        i = i + 1
        str1 ="["+str(i)+"] "+ job+"--"+company+"--"+address+"--"+wages+"--"+date+"\n"
        data_to_txt(str1,jobname)#存到文本
        data_to_sqlite(id, job, company, address, wages, date,jobname)#存到数据库
        print(str1)


def urlformat(urlstart):
    """
    返回{}.html格式字符串
    """
    url = re.sub('1.html','{}.html',urlstart)
    return url

def get_page_html(page_num,urlstart):
    """
    输入中页数，返回每一页的url
    """
    list=[]
    for i in range(page_num):
        url = urlformat(urlstart)
        url = url.format(i)
        list.append(url)
    return list

def all_job_get():
    """
    输入多个职位名称及第一页url批量抓取
    """
    for data in urldict:
        jobname = data['jobname']
        urlstart = data['urlstart']
        html = url_input(urlstart)
        all_page_num = int(find_all_page(html))
        print("+++++++++++++++++%s++++++++++++++++++++" % (all_page_num))
        urllist = get_page_html(all_page_num, urlstart)
        for url in urllist:
            html = url_input(url)
            data_items = find_data(html)
            print_items(data_items, jobname)
        i = 0#批量抓取后换个职位重新计数
def one_job_get():
    """
    单个职位信息抓取
    """
    html = url_input(urlstart)#获取首页
    all_page_num = int(find_all_page(html))#从首页获取总共页数
    print("+++++++++++++++++%s++++++++++++++++++++" % (all_page_num))
    urllist = get_page_html(all_page_num, urlstart)#获取每一页url存到列表里
    for url in urllist:#从列表里迭代每一页url
        html = url_input(url)#获取页面url
        data_items = find_data(html)#查找信息返回职位等信息
        print_items(data_items, jobname)#将信息存到文本信息和数据库
    i = 0

if __name__ == '__main__':
    all_job_get()
    # one_job_get()
