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
result = 0
i = 0

while result > min(evol) - max(evol):
    if result > min(evol[evol.index(max(evol)):]) - max(evol):
        result = min(evol[evol.index(max(evol)):]) - max(evol)
    evol.pop(evol.index(max(evol)))
    
print result