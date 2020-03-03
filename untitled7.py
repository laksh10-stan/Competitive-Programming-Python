# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:52:24 2020

@author: laksh
"""

import math
for _ in range(int(input())):
    l, r = map(int, input().split())
    a, s = l, l
    #print(int(math.log(l,2)))
    m=int(math.log(l,2))+1
    for i in range(l+1, 2**m):
        a &= i
        s = s%(10**9 + 7)
        s += a
        if a == 0:
            break
    print(s)