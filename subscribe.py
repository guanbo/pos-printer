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
import threading
import subprocess
from utils import serial
import time

startup = time.time()
def message_handler(message):
    if (message):
        if message['type'] == 'message': 
            print message['channel'], ":", message['data']
            lpr =  subprocess.Popen(["python", "print.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            lpr.communicate(message['data'])
        else:
            now = time.time()
            print now, ":startup:", now-startup, ":", message
    

if __name__ == "__main__":
    r = redis.StrictRedis(host='service.fankahui.com',socket_timeout=5)
    ps = r.pubsub()
    channel = serial.getserial()
    if (channel == "ERROR000000000"):
        channel = "000000007985f65b"
    ps.subscribe(channel)
    
    while True:
        # message = ps.get_message()
        # message_handler(message)            
        # time.sleep(0.001)  # be nice to the system :)
        for message in ps.listen():
            message_handler(message)