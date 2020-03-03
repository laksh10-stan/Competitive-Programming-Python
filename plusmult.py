# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:24:14 2019

@author: laksh
"""

for i in range(int(input())):
    n, l  = int(input()), list(map(int,input().split()))
    print((((l.count(2)-1)*l.count(2))//2)+(((l.count(0)-1)*l.count(0))//2))