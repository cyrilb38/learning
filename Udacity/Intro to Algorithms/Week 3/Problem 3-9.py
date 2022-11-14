# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 18:09:32 2016

@author: Cyril
"""

def number_of_descendants(S, root):
    #Create the results dictionnary with every entry of S    
    G = {}    
    for key in S:
        G[key] = 0
    #Create 3 lists :
    visited = [] # 1st loop to know which node are visited
    toExplore = [root] # contain the node that needs to be explored (1st loop)
    toReExplore = [] # contain the node that needs to be explored (2nd loop)
    known = [] #contains a list of nodes where we know all the descendants
    # Explore S dico for a 1st loop, to get the nodes with no descendants    
    while len(toExplore):
        node = toExplore[0]
        visited.append(node)
        boolOk = True
        for subNode in node:
            if S[node][subNode] == "green" and subNode not in visited:
                boolOk = False
                toExplore.append(subNode)
        if boolOk:
            
        if not boolOk:
            toReExplore.append(node)
            
       
       

       
            

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}
    