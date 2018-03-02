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
        def __init__(self, toUserName, fromUserName, content):
            '''
            1、 __dict__是一个字典，键是属性名，值为属性值。
            2、foo(**{"a":2,"b":3,"c":4,"d":5})#**{"a":2,"b":3,"c":4,"d":5}是将字典里的每个值按照关键字传值的方式传给a,b,c,d
            '''
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
