# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 8:40
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : wordrate.py
# @Software: PyCharm 统计单词频率并且画图统计

import string
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm

hist = []
def process_line(line,hist):
    for word in line.split():#根据空格将每一行分为每个单词
        word = word.strip(string.punctuation+string.whitespace)#将每个单词后面的标点符号和空格除去
        word = word.lower()#转成小写
        hist.append(word)#将单词添加到hist列表里
with open('english.txt','r') as f:
    for line in f:
        process_line(line,hist)

res = {}
for word in hist:
    '''
    批量注释ctrl+ / 统计单词出现次数
    '''
    # if word not in res:
    #     res[word] = 1
    # else:
    #     res[word]= res[word] + 1
    res[word] = res.get(word,0)+1

t = []
for key, value in res.items():
    """
    列表取出key value 按照逆序排序
    """
    t.append([value,key])
t.sort(reverse=True)


for i in range(10):
    plt.bar(t[i][1:],t[i][:-1])#数据切片

ZH = fm.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
plt.legend(prop=ZH)#完成数据加载
plt.xlabel(u'单词',fontproperties=ZH)
plt.ylabel(u'频率',fontproperties=ZH)
plt.title(u'统计单词出现的频率',fontproperties=ZH)
plt.savefig("D:\word.png",dpi=100)
plt.show()