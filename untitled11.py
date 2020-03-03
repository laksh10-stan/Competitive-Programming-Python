# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:56:18 2020

@author: laksh
"""
for i in range (int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s=0
    K=0
    for j in range(len(a)):   
        K += min(min(a), min(b))
        #L, idx = closest(b, K)
        #s += min(K, L)
        a.remove(min(a))
        b.remove(min(b))
    print(K)