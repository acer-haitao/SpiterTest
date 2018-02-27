#!/usr/bin/python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: main.py
# Author: yuhaitao
# mail: acer_yuhaitao@163.com
# Created Time: Tue 27 Feb 2018 10:24:29 PM CST
#########################################################################
import web
from handle import handle
urls = (
    '/','handle'    
    )
#class index(object):
#   def GET(self):
#        return "Hello Test"
if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()

