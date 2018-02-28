# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:19:54 2017

@author: hp
"""
import math
i=-19437
for n in range(1,13):
    i=i+52444.17*(math.pow(1.12,-n))
print(i)