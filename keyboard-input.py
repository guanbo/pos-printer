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

import sys, httplib
from evdev import InputDevice, list_devices, ecodes, events
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-H", "--host", 
                  action="store", dest="host", type="string", default="127.0.0.1",
                  help="host or ip which register to listen keyboard")
parser.add_option("-p", "--port",
                  action="store", dest="port", default=9000,
                  help="port on which register to listen")
parser.add_option("-r", "--route",
                  action="store", dest="route", type="string", default="/",
                  help="port on which register to listen")

(options, args) = parser.parse_args()
print options

devices = map(InputDevice, list_devices())
dev = InputDevice('/dev/input/event0')
for d in devices:
    if 'Keyboard' in d.name:
        print d
        dev = d
        
barcode = ''

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = events.KeyEvent(event)
        if key_event.keystate == events.KeyEvent.key_up:
            if key_event.keycode == 'KEY_ENTER':
                print 'barcode=', barcode, "to ", options.host, options.port, options.route
                try:
                    conn = httplib.HTTPConnection(options.host, options.port)
                    conn.set_debuglevel(1)
                    conn.request("POST", options.route, barcode)
                    conn.close()
                except:
                    print "Error when post barcode"
                barcode = ''
            else:
                barcode += str((key_event.scancode-1)%10)
