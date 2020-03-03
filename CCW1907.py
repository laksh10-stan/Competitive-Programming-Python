# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:50:40 2019

@author: laksh
"""
from sympy import primerange
t=int(input())
for i in range(t):
    n=int(input())
    o=n+1
    f=1
    while(n>0):
        f*=n
        n-=2
    print(f)
    c=0
    l=list(primerange(1,o))
    print(l)
    for k in range (len(l)):
        if f%l[k]==0:
            #print(l[k])
            c+=1
    print(c) 