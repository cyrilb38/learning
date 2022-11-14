# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 10:53:28 2016

@author: Cyril
"""

import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    l = range(0,100,2)
    return random.choice(l)

        
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    l = range(0,12,2)
    new_l = [x+9 for x in l]
    return random.choice(new_l)
    

print range(1)

random.seed(9001)
d = random.randint(1, 10)
for i in xrange(random.randint(1, 10)):
    if random.randint(1, 10) < 7:
        print d
    else:
        random.seed(9001)
        d = random.randint(1, 10)
        print random.randint(1, 10)