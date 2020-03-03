# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:19:47 2019

@author: laksh
"""

t = int(input())
for i in range (t):
    n=int(input())
    c=0
    l=list(map(int,input().split()))
    for j in range (len(l)):
        if j==0:
            c+=1
        elif (j == 1 or j == 2 or j == 3 or j == 4 or j == 5) and (min(l[0:j])>l[j]):
            c+=1
        elif j>5:
            if min(l[j-5:j])>l[j]:
                c+=1
    print(c)
            