# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import re

def compte_chiffre ():
    my_file = open("Data/Actual data - 98 - 667.txt")
    numbers = []
    for line in my_file:
        line = line.rstrip()
        numbers += re.findall("([0-9]+)",line)
    result = 0    
    for i in numbers:
        result += int(i)
    return result