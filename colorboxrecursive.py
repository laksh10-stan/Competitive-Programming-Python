# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:00:05 2019

@author: laksh
"""

def md(l, n, m, j, s, c, d):
    if j < m-1:
        for i in range (n//m):
            e = min(c, l[j][i])
            f = max(d, l[j][i])
            print(i, j)
            s = md(l, n, m, j+1, s, e, f)
    else:
        for i in range(n//m):
            print(l[j][i])
            print(c, d)
            e = min(c, l[j][i])
            f = max(d, l[j][i])
            if s > f-e:
                s = f-e
            print(i, j, s)
        return s
for _ in range (int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    l1 = []
    s, c, d = 10**9, 10**9+1, 0
    for i in range(m):
        l2 = []
        for j in range(n//m):
            l2.append(l[i+j*m])
        l1.append(l2)
    j = 0
    print(md(l1, n, m, j, s, c, d))