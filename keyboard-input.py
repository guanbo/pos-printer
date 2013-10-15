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

import sys, httplib, tempfile
from evdev import InputDevice, list_devices, ecodes, events

print sys.argv

# regfile = "minisrv-register.conf"
# if sys.argv.count >= 2:
regfile = sys.argv[1]
registerfile = open(regfile, "rb")

devices = map(InputDevice, list_devices())
dev = InputDevice('/dev/input/event0')
for d in devices:
    if 'Keyboard' in d.name:
        print d
        dev = d
        
barcode = ''

def getSlaver():
    registerfile.seek(0)
    print "Read stdin", registerfile.read()
    slaver = {"host":"192.168.0.7", "port":9000, "path":"/barcode"}
    return slaver
     
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = events.KeyEvent(event)
        if key_event.keystate == events.KeyEvent.key_up:
            if key_event.keycode == 'KEY_ENTER':
                slaver = getSlaver()
                print 'barcode=', barcode
                conn = httplib.HTTPConnection(slaver["host"], slaver["port"])
                conn.request("POST", slaver["path"], barcode)
                barcode = ''
            else:
                barcode += str((key_event.scancode-1)%10)
