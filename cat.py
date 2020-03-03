# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:19:22 2019

@author: laksh
"""

t=int(input())
for i in range (t):
    x=0
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    final = [l[p * n:(p + 1) * n] for p in range((len(l) + n - 1) // n )]  
    flag = 0 
    for j in range (len(final)):
        flag = len(set(final[j])) == len(final[j]) 
        if(flag) : 
            z=0
        else :
            x+=1
    if(x==0):
        print("YES")
    else:
        print("NO")
    