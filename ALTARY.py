# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:28:46 2019

@author: laksh
"""
def Max(l,k):
    cw=1
    for j in range (len(l)-1):
        if((l[j]>0 and l[j+1]<0)or(l[j]<0 and l[j+1]>0)):
            cw+=1
        else:
            return cw
    return cw
t=int(input())
for i in range (t):
    s=int(input())
    l=list(map(int,input().split()))
    k=0
    ct=[]
    while(len(l)>0):
        ct.insert(k,Max(l,k))
        k+=1
        del l[0]   
    print (' '.join(map(str, ct)))