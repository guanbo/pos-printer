#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Copyright (c) 2013 Guan Bo <guanbo2002@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import subprocess
import socket
import fcntl
import struct
from datetime import *
from utils import serial
import shelve

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def print_usb_test():
    try:
        ip = get_ip_address('eth0')
        data_string="\
\n\n\
\x1b\x61\x01\x1b\x21\x30打印机自动检测\n\
\x1b\x61\x00\x1b\x21\x00\n\
--------------------------------\n\
自检时间："+date.today().isoformat()+"\n\
设备序列号："+serial.getserial()+"\n\
打印机IP地址："+ip+"\n\n\
泛盈科技 版权所有\n\
发布时间：2013-09-24\n\
--------------------------------\n\
\n\n\n\n"
        lpr =  subprocess.Popen(["python", "print.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        lpr.communicate(data_string)
    except:
        pass
       

def print_net_test():
    config = shelve.open("config")
    if config.has_key('printerip') == True:
        print '-----',config["printerip"]
        netdata_string = "\
\n\n\
\x1b\x61\x01\x1b\x21\x30打印机自动检测\n\
\x1b\x61\x00\x1b\x21\x00\n\
--------------------------------\n\
自检时间："+date.today().isoformat()+"\n\
IP地址："+config["printerip"]+"\n\n\
泛盈科技 版权所有\n\
--------------------------------\n\
\n\n\n\n\x1d\x56\x00"
        lpr2 =  subprocess.Popen(["python", "netprint.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        lpr2.communicate(netdata_string)
    
if __name__ == "__main__":
    print_usb_test()
    print_net_test()