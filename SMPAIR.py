# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:56:45 2019

@author: laksh
"""

t=int(input())
for i in range(t):
    s=int(input())
    l=list(map(int,input().split()))
    sm=list()
    for j in range(len(l)-1):
        sm.append(l[j]+l[j+1])
    print(min(sm))
        