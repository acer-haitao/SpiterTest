#!/usr/bin/python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: handle.py
# Author: yuhaitao
# mail: acer_yuhaitao@163.com
# Created Time: Tue 27 Feb 2018 10:55:59 PM CST
#########################################################################
import web
import hashlib

class handle(object):
    def GET(self):
        try:
            data = web.input()
            print data
            #if len(data) == 0:
            #    return "hello this handle"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "haitao"

            #list = [token,timestamp, nonce]
            #list.sort()
            #shal = hashlib.sha1()
            #map(sha1.update,list)
            #hascode = sha1.hexdigest()
            #print "handle/GET func: hashcode, signature: ", hashcode, signature
            #if hashcode == signature:
            if 1 > 0:
                return echostr
            else:
                return " "
        except Exception,Argument:
                return Argument

