# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 8:48
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : udp.py
# @Software: PyCharm
import datetime
import struct
from socket import *
from time import *

import MySQLdb


def add_mysql(MAC, dev_float, uptime, fromip):
    connect = MySQLdb.connect('mysql.litianqiang.com', 'novel', 'qiangzi()', 'test', port=7150, charset="utf8")
    cursor = connect.cursor()
    sql = 'insert into devapp_dev_data(MAC,dev_float,uptime,fromip) VALUES ("{MAC}",{dev_float},"{uptime}","{fromip}");'.format(
        MAC=MAC, dev_float=dev_float, uptime=uptime, fromip=fromip)
    # sql = 'CREATE DATABASE IF NOT EXISTS dev_test DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
    try:
        cursor.execute(sql)
        connect.commit()
    except Exception as e:
        print("SQLERRO", e)
        connect.close()
        pass


def udp():
    Host = '192.168.3.90'
    PORT = 8899
    BUFSZ = 1024
    ADDR = (Host, PORT)
    udpserSock = socket(AF_INET, SOCK_DGRAM)
    udpserSock.bind(ADDR)
    while True:
        data, addr = udpserSock.recvfrom(BUFSZ)
        MAC = data[8:20].decode()  # 将bytes转换成str
        dev_data = data[20:24]
        dev_float = struct.unpack('<f', struct.pack('4B', *dev_data))[0]
        time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(MAC, dev_float, ctime(), addr[0])
        add_mysql(MAC, dev_float, time1, addr[0])


if __name__ == '__main__':
    udp()
