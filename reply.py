# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 10:54
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : reply.py
# @Software: PyCharm

import time
class Msg(object):
    def __init__(self):
        pass
    def send(self):
        return "success"

class TextMsg(Msg):
    try:
        def __init__(self, toUserName, fromUserName, content):
            self.__dict = dict()
            self.__dict['ToUserName'] = toUserName
            self.__dict['FromUserName'] = fromUserName
            self.__dict['CreateTime'] = int(time.time())
            self.__dict['Content'] = content
        def send(self):
            XmlForm = """
            <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{Content}]]></Content>
            </xml>
            """
            print("发送消息:")
            return XmlForm.format(**self.__dict)
    except Exception,e:
        print("TextMsgErro:",e)

class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return XmlForm.format(**self.__dict)
