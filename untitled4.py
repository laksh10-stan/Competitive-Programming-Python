# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:37:23 2020

@author: laksh
"""

for i in range(int(input())):
    n,a,b,c = map(int, input().split())
    l = list(map(int, input().split()))
    q=0
    y=10**9
    for j in range(len(l)):
        if (l[j] > a and l[j] < b) or (l[j] < a and l[j] > b):
            y = abs(a-b)+c
            print("y", y)
            break
        else:
            z = min(abs(b-l[j]), abs(a-l[j])) + c
            if(z<y):
                y = z
                print("y2", y)
    print(y)
            