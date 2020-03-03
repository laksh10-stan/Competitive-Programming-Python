# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:49:34 2020

@author: laksh
"""

for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    for j in range (len(a)):
        s += a[j]%k
        #if (s < (k-a[j]%k)) and (a[j]%k != 0) :
            #s += a[j]%k 
            #a[j] -= k-a[j]%k
        #else:
            #a[j] += k-a[j]%k
            #s -= k-a[j]%k
    y=len(a) - 1
    while y != 0:
        if s >= k:
            #a[y]+= k
            s -= k
        else:
            break
    print(s)