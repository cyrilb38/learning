# -*- coding: utf-8 -*-
"""
Created on Sun May 01 09:44:14 2016

@author: Cyril
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
evol = []
n = int(raw_input())
for i in raw_input().split():
    v = int(i)
    evol.append(v)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
i = 0
result = 0

while i < len(evol) and (min(evol[i:]) - max(evol[i:])) < result :
    if (min(evol[i:]) - evol[i]) < result:
        result = (min(evol[i:]) - evol[i])
    i+=1

print result