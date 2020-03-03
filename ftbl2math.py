# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:06:40 2019

@author: laksh
"""

t=int(input())
for i in range (t):
    n=int(input())
    l=[]
    for j in range(n):
        c,a,b=map(int,input().split())
        if(c==1):
            print("YES")
        else:
            