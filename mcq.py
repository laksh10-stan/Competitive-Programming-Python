# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:57:55 2019

@author: laksh
"""

t=int(input())
for i in range(t):
    s=int(input())
    r=str(input())
    w=str(input())
    l=len(r)
    m=0
    j=0
    while(l>j):
        if(r[j]==w[j]):
            m+=1
        elif(w[j]=='N'):
            m+=0
        else:
            j+=1
        j+=1
    print(m)       
            
            
    
    
    