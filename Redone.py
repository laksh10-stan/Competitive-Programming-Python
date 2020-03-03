# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:55:05 2019

@author: laksh
"""

t=int(input())
s=[]
for i in range(t):
    s.insert(i,int(input()))
    l=[]
    temp=1
    for j in range(s[i]):
        l.insert(j,temp)
        temp+=1
    el=0
    for k in range (len(l)-1):
        el=l[0]+l[1]+(l[0]*l[1])
        del l[0]
        del l[0]
        l.insert(0,el)
    print(l[0]%1000000007)

    