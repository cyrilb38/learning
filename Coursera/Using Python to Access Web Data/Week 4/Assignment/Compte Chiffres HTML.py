# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 18:32:45 2015

@author: Cyril
"""

import urllib
from BeautifulSoup import *


url = "http://python-data.dr-chuck.net/comments_207594.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)


# Retrieve all of the anchor tags
tags = soup('span')
result = 0
for tag in tags:
    result += int(tag.contents[0])

print result