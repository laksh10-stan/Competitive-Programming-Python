# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:02:44 2020

@author: laksh
"""
for i in range(int(input())):
    m,n = map(int, input().split())
    print(m & n)
    for j in range(min(m,n), max(m,n)+1):
        
        