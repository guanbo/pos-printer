#!/usr/bin/env python

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

import subprocess, sys
from escpos import *

# upstream_data = open("gb2312.txt").read()
input_data = sys.stdin.read()
# input_data = open("utf8.txt").read()
upstream_data = input_data.decode('utf-8').encode('gb2312')
# print 'print subprocess:', upstream_data

# Epson = printer.Usb(0x1cb0,0x0003)
Epson = printer.Usb(0x8866,0x0100, 0, 0x82, 0x02)
Epson.set()
Epson.text(upstream_data)

