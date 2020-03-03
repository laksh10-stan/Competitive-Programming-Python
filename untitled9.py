# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:39:15 2020

@author: laksh
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:19:00 2020

@author: laksh
"""
# import numpy as np 
# # cook your dish here
# def closest(lst, K): 
#     lst = np.asarray(lst) 
#     idx = (np.abs(lst - K)).argmin() 
#     return lst[idx] , idx
for i in range (int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    # s=0
    K=0
    for j in range(len(a)):   
        K += min(a[j] , b[j])
        # L, idx = closest(b, K)
        # s += min(K, L)
        # a.remove(min(a))
        # b.remove(b[idx])
    print(K)