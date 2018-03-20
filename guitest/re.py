# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 14:44
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : re.py
# @Software: PyCharm
import re

str = "This is That"
tmp = re.finditer('(th\w+)', str, re.I)
print(tmp.next().group())
print(tmp.next().group())
