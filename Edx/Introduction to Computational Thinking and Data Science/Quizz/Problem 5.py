# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 14:29:59 2016

@author: Cyril
"""

import pylab, random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    positiveTrials = 0
    for i in range(numTrials):
        bucket = [1,1,1,1,0,0,0,0]
        result = []
        for i in range(3):
            b = random.choice(bucket)
            result.append(b)
            bucket.remove(b)
            
        if sum(result) == 3 or sum(result) == 0:
            positiveTrials += 1
    
    return positiveTrials / float(numTrials)
    
xCoord = []    
yCoord = []
yProb = []  
prob = 1/7
for i in range(7):
    yCoord.append(drawing_without_replacement_sim(10**i))
    yProb.append(float(prob))
    xCoord.append(10**i)

pylab.plot(xCoord,yCoord,'r-',xCoord,yProb,'bo')
pylab.show
    