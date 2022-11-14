# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 10:30:29 2016

@author: Cyril
"""

inFile = open("julyTemps.txt","r")

high = []
low = []

for line in inFile :
    fields = line.split(" ")
    if len(fields) < 3 or not fields[0].isdigit():
        print fields
        
        
