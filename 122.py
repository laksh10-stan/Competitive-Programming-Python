# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:00:37 2019

@author: laksh
"""

t=int(input())
for i in range (t):
    n=int(input())
    l=[]
    c=0
    for j in range (1,n+1):
        print(j)
        print(n%j)
        if n%j not in l:
            l.append(n%j)
            c+=1
            print(l)
    #print(l)       
    print(len(l))
    print(c)
        
        
        
    