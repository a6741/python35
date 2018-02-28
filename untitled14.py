# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 20:15:41 2017

@author: hp
"""
import math
l=31
t=0
print("*****************************",l)
for xx in range(5):
    i=1
    x=xx+12
    px=math.exp(-(pow((x-14),2)/2))/pow(2*math.pi,0.5)
    for r in range(l+1):
        k=1
        for p in range(r):
            k=k*(p+1)
        i=i-(math.exp(-x)*math.pow(x,r))/k
    ll=px*i
    t+=ll
fei=t*10*73/6+1.25*(l-14)
print("%.1f"%fei)