# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:41:18 2016

@author: Cyril
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float("NaN")
    
    avg = 0
    Lnum = []
    for element in L:
        Lnum.append(len(element))

    avg = sum(Lnum) / len(Lnum)
    print Lnum
    result = 0
    for i in Lnum:
        result += (avg - i)**2
        
    return (result/len(L))**(0.5)
    
    
print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])