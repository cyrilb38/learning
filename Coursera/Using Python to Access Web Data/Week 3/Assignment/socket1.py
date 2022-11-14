# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 21:03:01 2015

@author: Cyril
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()


import urllib
x = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')