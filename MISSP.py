# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:28:24 2019

@author: laksh
"""

t=int(input())
for i in range(t):
    l=int(input())
    y=[]
    z=[]
    for j in range (l):
        y.append(int(input()))
        if y[j] not in z:
            z.append(y[j])
    x=[]
    u=len(z)
    for f in range(u):
        x.insert(f,0)
        for g in range (l):
            if z[f]==y[g]:
                x[f]+=1
    v=len(x)
    for k in range(v):
        if x[k]%2!=0:
            print(z[k])
        
    