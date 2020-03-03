# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:26:46 2019

@author: laksh
"""

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    i, m, a = 1, 0, 0
    while i < n:
        if l[i]-l[i-1] > 1:
            if a == 0:
                m += 1
            if l[i]-l[i-1] == 2:
                if i == n-1:
                    if a == 1:
                        m += 1
                a = 1
            else:
                a = 0
                if i == n-1:
                    m += 1
        else:
            a = 1
        i += 1
    print(m)