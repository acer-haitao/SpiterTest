# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 16:38
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : 51job.py
# @Software: PyCharm
import urllib
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

i = 0#统计爬取总条目
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
    #print(html)
    reg = re.compile(r'<span class="td">(.*?)</span><input id="jump_page" class="mytxt" type="text" value="1"/>',re.S)
    page_all = re.findall(reg, html)
    num = re.sub("\D", "", page_all[0])#从共5页中提取数字
    return num
def data_to_txt(str):
    with open(u"51job北上广深python.txt",'a+') as f:
        f.write(str)
def print_items(data_items):
    global i
    for data in data_items:
        job = data[0]
        company = data[1]
        address = data[2]
        wages = data[3]
        date = data[4]
        i = i + 1
        str1 ="["+str(i)+"] "+ job+"--"+company+"--"+address+"--"+wages+"--"+date+"\n"
        data_to_txt(str1)
        print(str1)

def urlformat(urlstart):
    url = re.sub('1.html','{}.html',urlstart)
    return url
def get_page_html(page_num,urlstart):
    list=[]
    for i in range(page_num):
        url = urlformat(urlstart)
        url = url.format(i)
        list.append(url)
    return list

if __name__ == '__main__':
    #python
    #urlstart = 'http://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    #嵌入式
    #urlstart = 'http://search.51job.com/list/010000,000000,0000,00,9,99,%25E5%25B5%258C%25E5%2585%25A5%25E5%25BC%258F%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    #云计算
    #urlstart ='http://search.51job.com/list/010000,000000,0000,00,9,99,%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    #机器学习
    #urlstart = 'http://search.51job.com/list/010000,000000,0000,00,9,99,%25E6%259C%25BA%25E5%2599%25A8%25E5%25AD%25A6%25E4%25B9%25A0,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    #人工智能
    #urlstart = 'http://search.51job.com/list/010000,000000,0000,00,9,99,%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    #自动驾驶
    #urlstart = 'http://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E9%25A9%25BE%25E9%25A9%25B6,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    #北上广深python
    urlstart = 'http://search.51job.com/list/010000%252C040000%252C020000%252C030200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    html = url_input(urlstart)
    all_page_num = int(find_all_page(html))
    print("+++++++++++++++++%s++++++++++++++++++++"%(all_page_num))
    urllist = get_page_html(all_page_num,urlstart)
    for url in urllist:
        html = url_input(url)
        data_items = find_data(html)
        print_items(data_items)

