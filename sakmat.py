# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:03:33 2019

@author: laksh
"""
import numpy as np
for i in range (int(input())):
    n,m,q=map(int,input().split())
    l=[[0]*m for _ in range (n)]
    #print(l)
    for j in range(q):
        x,y=map(int,input().split())
        for k in range (m):
            #print(x-1)
            #print(k)
            #print(l[0][k])
            #print(l[0])
            l[x-1][k]+=1
            #l[k][x-1]=l[k][x-1]+1
            #print(l)
        for k in range (n):
            l[k][y-1]+=1
            #print(l)
        print(l)
    l2=np.array(l)
    print(len(l2[l2%2!=0]))
    
        
        
        
        
        
        
    
    