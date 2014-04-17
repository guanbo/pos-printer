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

import redis  
import time

# import os,sys  
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
# sys.path.insert(0,parentdir)
# from utils import serial
  
rc = redis.Redis(host='service.fankahui.com')  
  
data_string="\
\n----------------------------\n\
\x1b\x61\x01\x1b\x21\x20\x1b\x21\x30泛盈科技\n\
\x1b\x61\x00\x1b\x21\x00总店\n\
时间 2013-09-24 18:19\n\
流水号 3 终端 100001 收银员 2\n\n\
\x1b\x44\x10\x16\x00\
商品\x09数量\x09金额\n\
-----------------------------\n\
iPhone 5\x094\x0918000.00\n\
iPhone 4S\x092\x096400.00\n\
iPhone 4S\x092\x097580.00\n\
一欄咖啡\x091\x090.9\n\
一咖啡\x091\x090.9\n\
-----------------------------\n\
合计 31980.90\n\
折扣 0.00\n\
应收 31980.90\n\
实收 32000.90\n\
找零 20.00\n\
"
if __name__ == "__main__":
    for n in range(3):
        rc.publish("000000007985f65b", data_string+"\ntimes:"+str(n))  
        time.sleep(5)
        # print serial.getserial()
