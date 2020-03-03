# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:35:25 2019

@author: laksh
"""

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    k=0
    while len(l)!=0:
        s+=(min(l)-k)*len(l)
        k=min(l)
        #print(s)
        h=l.index(min(l))
        #print(h)
        l=l[:h]
        #print(l)
        
    print(s)