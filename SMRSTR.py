# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 00:20:41 2019

@author: laksh
"""
t=int(input())
for p in range (t):
    n,q=map(int,input().split())
    l=list(map(int,input().split()))
    qu=list(map(int,input().split()))
    r=[]
    for i in range (len(qu)):
        temp=qu[i]
        for j in range(len(l)):
            temp//=l[j]
        r.insert(i,temp)
    print(r)