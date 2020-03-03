# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:17:48 2019

@author: laksh
"""

t = int(input())
for i in range(t):
    b=float(input())
    if(b<1500):
        hra=0.1*b
        da=0.9*b
    else:
        hra=500
        da=0.98*b
    gs=b+hra+da
    print(gs)