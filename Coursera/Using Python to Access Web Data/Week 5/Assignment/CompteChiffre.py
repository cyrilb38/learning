# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 19:17:17 2015

@author: Cyril
"""

import urllib
import xml.etree.ElementTree as ET
import ssl

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
url = "http://python-data.dr-chuck.net/comments_207591.xml"


data = urllib.urlopen(url, context=scontext).read()
tree = ET.fromstring(data)

result = 0
counts = tree.findall('.//count')

for count in counts:
    result += int(count.text)
    
print result