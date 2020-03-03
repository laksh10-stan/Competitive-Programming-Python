# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:03:51 2019

@author: laksh
""" 
t=int(input())
for i in range(t):
    r,c=map(int, input().split())
    m=[[]]
    for j in range(r):
        m.insert(j,list(map(int,input().split())))
    count=0
    for k in range(r):
        for x in range(c):
             if ((k==0 and x==0) or (k==r-1 and x==c-1) or (k==0 and x == c-1) or (k==r-1 and x==0)):
                 if(m[k][x]<2):
                     count+=1
             elif((k==0 and x!=0 and x!=c-1)or(k==r-1 and x!=0 and x!=c-1)or(x==0 and k!=0 and k!=r-1)or(x==c-1 and k!=0 and k!=r-1)):
                 if(m[k][x]<3):
                     count+=1
             else:
                 if(m[k][x]<4):
                     count+=1
    if(count==r*c):
        print('Stable')
    else:
        print('Unstable')
                 
        
            
        
        