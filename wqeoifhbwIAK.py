# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 21:51:28 2020

@author: laksh
"""

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = []
    li = []
    for i in range(n):
        l.append(str(input()))
        li.append(list(l[i]))
    print(l)
    print(li)