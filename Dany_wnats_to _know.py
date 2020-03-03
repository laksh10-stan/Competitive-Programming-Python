# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:38:17 2019

@author: laksh
"""

n,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range (n):
    s,e=map(int,input().split())
    s-=1
    sm=0
    for j in range(s,e):
        sm+=a[j]*b[j]
    print(sm)
        