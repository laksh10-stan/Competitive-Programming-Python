# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:43:50 2019

@author: laksh
"""

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = 0
    i = n-1
    while i >= 0:
        a = 0
        if l[i] == 1:
            if m < i:
                m = i
                break
        for j in range(i):
            if l[j]%l[i] == 0:
                a += 1
        if m < a:
            m = a
        if m >= i:
            break
        i -= 1
    print(m)