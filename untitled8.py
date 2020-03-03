# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:31:44 2020

@author: laksh
"""


# Python3 program to find Closest number in a list 
  
def closest(lst, K): 
      
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 
      
# Driver code 
lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8] 
K = 9.1
print(closest(lst, K))

import numpy as np 
# cook your dish here
def closest(lst, K): 
    lst = np.asarray(lst) 
    idx = (np.abs(lst - K)).argmin() 
    return lst[idx] , idx
for i in range (int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s=0
    for j in range(len(a)):   
        K = min(a)
        L, idx = closest(b, K)
        s += min(K, L)
        a.remove(min(a))
        b.remove(b[idx])
    print(s)