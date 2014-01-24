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

import subprocess, sys, os
from escpos import *
from lsusb import *

prefix = "/sys/bus/usb/devices/"
adapters = "/etc/adapter-printers"

def read_usb():
	for dirent in os.listdir(prefix):
		#print dirent,
		if not dirent[0:3] == "usb":
			continue
		usbdev = UsbDevice(None, 0)
		usbdev.read(dirent)
		usbdev.readchildren()
        # print usbdev
        return usbdev

def usbprinter():
    # "find usb printer"
    usbdev = read_usb()
    printers = []
    with open(adapters) as f:
        printers = f.read().splitlines()
    for printer_name in printers:
        # print "Printer:", printer_name
        dev = usbdev.search(printer_name)
        if dev: 
            in_ep=0x82
            out_ep=0x01
            interface = dev.interfaces[0];
            for ep in interface.eps:
                if ep.direction == "in":
                    in_ep=ep.epaddr
                else:
                    out_ep=ep.epaddr
            # print "Found dev:", dev.name, dev.vid, dev.pid, in_ep, out_ep
            return printer.Usb(dev.vid, dev.pid, 0, in_ep, out_ep)
        
Epson = usbprinter()
# Epson.barcode('1324354657687','EAN13',64,2,'','')
# Epson.text("\x1b\x44\x10\x18"+chr(0))
# 
# cols = ['coloum1', 'coloum2', 'coloum3']
# for col in cols:
#     Epson.text(col)
#     Epson.control('ht')
# 
# Epson.text('\ntest done\n\n')
# Epson.control('lf')

input_data = sys.stdin.read()
upstream_data = input_data.decode('utf-8').encode('gb18030')
Epson.set()
Epson.text(upstream_data)

