# -*- coding: utf-8 -*-
"""
Created on Sat Dec 05 18:45:39 2015

@author: Cyril
"""


import urllib
from BeautifulSoup import *
import ssl

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Ava.html"

# Retrieve all of the anchor tags
iteration = 7
position = 18
while iteration > 0:
    html = urllib.urlopen(url, context=scontext).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position - 1].get('href', None)
    print url
    iteration -=1