# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 19:53:48 2015

@author: Cyril
"""

import json
import urllib

url = "http://python-data.dr-chuck.net/comments_207595.json "
info = urllib.urlopen(url).read()

data = json.loads(info)

results = 0

for element in data["comments"]:
    results += element["count"]
    
print results