# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 16:38
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : 51job.py
# @Software: PyCharm
import re
import sqlite3
import sys
import time
import urllib

import MySQLdb
import xlwt

from jobnameconfig import jobname, urlstart
from urlconfig import urldict

reload(sys)
sys.setdefaultencoding('utf8')#处理打印中文字体用Unicode编码

i = 0#统计爬取总条目
j = 1
def url_input(url):
    """
    获取网页源码html信息
    """
    num = 2
    try:
        get_html = urllib.urlopen(url)
        read_html = get_html.read().decode('gbk')
    except Exception as e:
        print(e)
        read_html = None
    return read_html

def find_data(html):
    """
    用正则表达式获取需要的信息
    """
    # reg = re.compile(r'class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S)
    reg = re.compile(
            r'class="t1 ">.*?<a target="_blank" title="(.*?)".*?href="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?href="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',
            re.S)

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


def find_txt(joburl):
    time.sleep(3)
    txt_html = url_input(joburl)
    reg = re.compile(r'<div class="bmsg job_msg inbox">(.*?)<div class="mt10">', re.S)
    txt_tmp1 = re.findall(reg, txt_html)
    p = re.compile(r'<[^>]+>')
    txt_tmp = p.sub('', str(txt_tmp1))

    tmp = txt_tmp.decode('raw_unicode-escape').encode('utf-8').replace("u'", '', 1)
    txt = tmp.replace("']", '').replace("[", '', 1).replace('\\t', '').replace('\\n', '').replace('', '').replace('\\r',
                                                                                                                  '')
    print(txt)
    return txt

# 一个例子掌握xlwt,设计要求见README文档
def set_style(name, height, bold=False):
    # 这部分设置字体样式
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    # 这部分设置居中格式
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
    style.alignment = alignment
    return style


def data_to_excel(filename, data_items, sheet1, workbook, jobtxt):
    try:
        global j
        # 从第二行开始写
        for data in data_items:  # 在循环里放入style设置报错more than 4094 xfs
            list = {'0': 0, '1': 2, '2': 4, '3': 5, '4': 6, '5': 1, '6': 3}
            for key, value in list.items():
                sheet1.col(int(key)).width = 256 * len(data[value].encode('utf-8'))  # 计算每一列的宽度
                sheet1.write(j, int(key), data[value])
            j = j + 1  # 下一列
        workbook.save(u'51job%s.xls' % (jobname))
    except Exception as e:
        print("EXCELERRO:", e)
        workbook.save(u'51EROjob%s.xls' % (jobname))
        pass


def data_to_sqlite(id, job, company, address, wages, date, jobname, joburl):
    """
    将信息存储到数据库
    """
    db = sqlite3.connect("D:\Python-Test\StuProject\db.sqlite3")
    cursor = db.cursor()  # OR IGNORE重复数据会跳过
    sql = "insert  OR IGNORE into 'job51_job51'(job,company,address,wages,date,jobname,joburl) values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % (
        job, company, address, wages, date, jobname, joburl)
    # sql = "insert OR IGNORE  into '51jobtest'(job,company,address,wages,date,jobname) values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % ("job", "company", "address", "wages", "date", "jobname")
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("SQLERRO:",e)


def data_to_sqlite_address(address):
    """
    将信息存储到数据库
    """
    db = sqlite3.connect("D:\Python-Test\StuProject\db.sqlite3")
    cursor = db.cursor()  # OR IGNORE重复数据会跳过
    sql = "insert  OR IGNORE into 'job51_jobadress'(address) values (\"%s\");" % (
        address)
    # sql = "insert OR IGNORE  into '51jobtest'(job,company,address,wages,date,jobname) values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % ("job", "company", "address", "wages", "date", "jobname")
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("SQLERRO:", e)


def data_to_sqlite_date(date):
    """
    将信息存储到数据库
    """
    db = sqlite3.connect("D:\Python-Test\StuProject\db.sqlite3")
    cursor = db.cursor()  # OR IGNORE重复数据会跳过
    sql = "insert  OR IGNORE into 'job51_jobdate'(jobdate) values (\"%s\");" % (
        date)
    # sql = "insert OR IGNORE  into '51jobtest'(job,company,address,wages,date,jobname) values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % ("job", "company", "address", "wages", "date", "jobname")
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("SQLERRO:", e)


def data_to_sqlite_jobname(jobname):
    """
    将信息存储到数据库
    """
    db = sqlite3.connect("D:\Python-Test\StuProject\db.sqlite3")
    cursor = db.cursor()  # OR IGNORE重复数据会跳过
    sql = "insert  OR IGNORE into 'job51_jobname'(jobname) values (\"%s\");" % (
        jobname)
    # sql = "insert OR IGNORE  into '51jobtest'(job,company,address,wages,date,jobname) values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % ("job", "company", "address", "wages", "date", "jobname")
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("SQLERRO:", e)


def data_to_mysql(id, job, company, address, wages, date, jobname, joburl):
    connect = MySQLdb.connect('mysql.litianqiang.com', 'novel', 'qiangzi()', 'test', port=7150, charset="utf8")
    cursor = connect.cursor()
    sql = """ insert  IGNORE  into job51_job51(job,company,address,wages,date,jobname,joburl) values ("{job}","{company}","{address}","{wages}","{date}","{jobname}","{joburl}");""".format(
            job=job, company=company, address=address, wages=wages, date=date, jobname=jobname,
            joburl=joburl)  # sql = 'CREATE DATABASE IF NOT EXISTS dev_test DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
    try:
        cursor.execute(sql)
        connect.commit()
    except Exception as e:
        print("SQLERRO", e)
        connect.close()
        pass


def data_to_txt(str,jobname):
    """
    将信息存储到文本
    """
    with open(u"51job%s.txt"%(jobname),'a+') as f:
        f.write(str)


def data_to_sqlite_jobwages(jobwages):
    """
      将信息存储到数据库
      """
    db = sqlite3.connect("D:\Python-Test\StuProject\db.sqlite3")
    cursor = db.cursor()  # OR IGNORE重复数据会跳过
    sql = "insert  OR IGNORE into 'job51_jobwages'(jobwages) values (\"%s\");" % (jobwages)
    # sql = "insert OR IGNORE  into '51jobtest'(job,company,address,wages,date,jobname) values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % ("job", "company", "address", "wages", "date", "jobname")
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("SQLERRO:", e)


def print_items(data_items,jobname):
    """
    从正则匹配后的列表中获取信息存储打印
    """
    global i
    for data in data_items:
        job = data[0]
        company = data[2]
        address = data[4]
        wages = data[5]
        date = data[6]
        alljoburl = data[3]
        thisjoburl = data[1]
        jobnametest_id = jobname
        i = i + 1
        # jobtxt = find_txt(thisjoburl)
        str1 = "[" + str(
                i) + "] " + job + "--" + company + "--" + address + "--" + wages + "--" + date + "--" + thisjoburl + "\n"
        data_to_txt(str1, jobname)  # 存到文本
        data_to_sqlite(id, job, company, address, wages, date, jobname, thisjoburl)  #存到数据库
        # data_to_sqlite(id, job, company, address, wages, date, jobname, thisjoburl, addresstest_id, jobdatetest_id,
        #                jobnametest_id, jobwagestest_id)  #
        # data_to_sqlite_address(address)
        # data_to_sqlite_date(date)
        # data_to_sqlite_jobname(jobname)
        # data_to_sqlite_jobwages(wages)
        data_to_mysql(id, job, company, address, wages, date, jobname, thisjoburl)
        print(str1)
        # return jobtxt


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
        time.sleep(1)
        i = 0#批量抓取后换个职位重新计数

def one_job_get():
    """
    单个职位信息抓取
    """
    html = url_input(urlstart)#获取首页
    all_page_num = int(find_all_page(html))#从首页获取总共页数
    print("+++++++++++++++++%s++++++++++++++++++++" % (all_page_num))
    urllist = get_page_html(all_page_num, urlstart)#获取每一页url存到列表里

    ####################################################
    workbook = xlwt.Workbook()  # 创建工作簿
    sheet1 = workbook.add_sheet('sheet_name', cell_overwrite_ok=True)  # 创建sheet,第二参数用于确认同一个cell单元是否可以重设值
    row0 = [u'职位', u'公司名称', u'地点', u'工资', u'日期', u'职位链接', u'其他岗位', u'职位要求']
    # 第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    ####################################################

    for url in urllist:#从列表里迭代每一页url
        html = url_input(url)#获取页面url
        data_items = find_data(html)#查找信息返回职位等信息
        jobtxt = print_items(data_items, jobname)  # 将信息存到文本信息和数据库
        data_to_excel(jobname, data_items, sheet1, workbook, jobtxt)

if __name__ == '__main__':
    all_job_get()
    #one_job_get()
