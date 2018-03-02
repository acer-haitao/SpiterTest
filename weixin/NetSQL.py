# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 11:23
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : NetSQL.py
# @Software: PyCharm
import sqlite3

def sqlitetest(num):
    try:
        cx = sqlite3.connect("D:\Python-Test\WeiXin\db.sqlite3")
        cursor = cx.cursor()
        sql = '''SELECT * FROM  comment_comment WHERE id = 44947+%s;'''%(num)
        cursor.execute(sql)
        results = cursor.fetchall()
        for i, row in enumerate(results):
            txt = row[1]
            footer = row[2]
            list ={
                'txt':txt,
                'footer':footer
            }
        return list
    except:
        return "erro"


