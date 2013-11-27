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

import subprocess, SimpleHTTPServer, SocketServer, os.path, time, sys
from escpos import *

PORT = 8000
keyboardhook = None

class PrinterServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
    '''Printer Server'''

    def do_POST(self):
        try:
            if self.path == '/register':
                global keyboardhook
                if keyboardhook is not None:
                    print "keyboardhook: ", keyboardhook.pid
                    keyboardhook.terminate()
                keyboardhook = subprocess.Popen(['python', 'keyboard-input.py', '--host', self.client_address[0]])
            elif self.path == '/update':
                subprocess.call(["./update-auto.sh"], stdout=self.wfile, stderr=self.wfile, shell=True)
            else:
                length = int(self.headers.getheader('content-length'))
                data_string = self.rfile.read(length)
                data_string += "\n"
                lpr =  subprocess.Popen(["python", "print.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                message, err = lpr.communicate(data_string)[1]
            statusCode = 201
        except ValueError:
            print "=====",ValueError
            statusCode = 400
        except:
            statusCode = 500 
        self.send_response(statusCode)

def start_server():
    """Start the server."""
    server = SocketServer.TCPServer(("", PORT), PrinterServer)
    print time.asctime(), "Printer serving START at port", PORT
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        pass
    server.server_close()
    print time.asctime(), "Printer serving STOP at port", PORT

if __name__ == "__main__":
    start_server()
