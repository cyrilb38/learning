# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 21:47:19 2016

@author: Cyril
"""

import pylab, random
import numpy as np

a = np.random.normal(size=1000)
b = np.random.normal(size=1000)
c = np.random.normal(size=1000)

pylab.hist((a,b,c))