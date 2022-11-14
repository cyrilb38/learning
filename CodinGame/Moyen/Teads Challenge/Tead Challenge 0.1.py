# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:54:41 2016

@author: Cyril
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # the number of adjacency relations
graph = {}
nodesToExplore = [] 

for i in xrange(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in raw_input().split()]
    if xi in graph:
        graph[xi].append(yi)
    else:
        graph[xi] = [yi]
        nodesToExplore.append(xi)
        
    if yi in graph:
        graph[yi].append(xi)
    else:
        graph[yi] = [xi]    
        nodesToExplore.append(yi)

best = n
i = 0

while i < len(nodesToExplore) and best > 1:
    maillage = [[nodesToExplore[i]]]
    explored = [nodesToExplore[i]]
    step = 0
    remaining = len(nodesToExplore)
    
    while step < best and remaining > 0:
        remaining -= len(maillage[step])
        if remaining > 0:
            for noeud in maillage[step]:
                for sousNoeud in graph[noeud]:
                    if sousNoeud not in explored:
                        if len(maillage) == step + 1:
                            maillage.append([sousNoeud])
                        else:
                            maillage[len(maillage)-1].append(sousNoeud)
                        explored.append(sousNoeud)
        step += 1
    
    best = step
    i += 1
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
print best - 1

# The minimal amount of steps required to completely propagate the advertisement

