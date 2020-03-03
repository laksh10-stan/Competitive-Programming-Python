# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:46:30 2019

@author: laksh
"""

t=int(input())
for i in range (t):
    n=int(input())
    s=1
    r=1
    while n>=1:
        #r%=1000000007
        r*=(s**n)
        #r%=1000000007
        s+=1
        n-=1
    print(r%1000000007)
        
        