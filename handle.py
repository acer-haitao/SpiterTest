#!/usr/bin/python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: handle.py
# Author: yuhaitao
# mail: acer_yuhaitao@163.com
# Created Time: Tue 27 Feb 2018 10:55:59 PM CST
#########################################################################
import web
import receive
import reply
import NetSQL
import types
class handle(object):
    def GET(self):
        try:
            data = web.input()
            print data
            echostr = data.echostr
            if 1 > 0:
                return echostr
            else:
                return " "
        except Exception,Argument:
                return Argument

    def POST(self):
        try:
            webData = web.data()
            print "接收客户信息:\n", webData
            # 后台打日志
            recMsg = receive.parse_xml(webData)#处理接收微信发过来的信息
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                recvtext = recMsg.Content#接收发送的信息
                if recMsg.MsgType == 'text':
                    try:
                        if recvtext.isdigit():#判断接收的是数字还是字符串
                            content = NetSQL.sqlitetest(recvtext)['txt'].encode('utf8') + "\n\n\n------来自网易云音乐评论------\n    %s"%(NetSQL.sqlitetest(recvtext)['footer'].encode('utf8'))#不转码报错ASCII
                            print(content)
                            replyMsg = reply.TextMsg(toUser, fromUser, content)
                            return replyMsg.send()
                        else:
                            content = "请发送数字:1-104180\nhttp://daydayup11.cn/"
                            replyMsg = reply.TextMsg(toUser, fromUser, content)
                            return replyMsg.send()
                    except Exception,e:
                        print("SendERR:",e)
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment


