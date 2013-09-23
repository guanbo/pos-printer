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

import subprocess, SimpleHTTPServer, SocketServer, os

PORT = 8000

def send_to_printer():
    upstream_data = open("gb2312.txt").read()
    lpr =  subprocess.Popen(["/usr/bin/lpr", "-h"], stdin=subprocess.PIPE)
    lpr.stdin.write(upstream_data)
        
class PrinterServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
    '''Printer Server'''
    send_print2= send_to_printer
    
    def send_print(self, upstream_data):
        '''Send data to printer'''
        # upstream_data = open("gb2312.txt").read()
        lpr =  subprocess.Popen(["python", "print.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # lpr.stdin.write(upstream_data)
        print lpr.communicate(upstream_data)
        print "send_print:", upstream_data
        
    def do_POST(self):
        length = int(self.headers.getheader('content-length')) 
        data_string = self.rfile.read(length)
        try:
            # lpr = subprocess.Popen(["/usr/bin/lpr", "-h"], stdin=subprocess.PIPE)
            # lpr.stdin.write(data_string)
            self.send_print(data_string)
            result = 201
        except ValueError:
            print ValueError
            result = 400
        except:
            result = 500
        self.send_response(result)

def start_server():
    """Start the server."""
    server = SocketServer.TCPServer(("", PORT), PrinterServer)
    print "Printer serving at port", PORT
    server.serve_forever()

if __name__ == "__main__":
    # send_to_printer()
    start_server()