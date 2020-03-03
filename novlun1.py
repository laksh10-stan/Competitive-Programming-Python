# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:19:27 2019

@author: laksh
"""

for i in range (int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    
    c=0
    p=0
    for j in range(n):
        
        #print('l',l)
        if (l[j] + c ) >= k:
            c = (l[j] + c) - k
            #print('c',c)
            p+=1
        else:
            print('NO ', j+1)
            break
    if p == n:
        print('YES')
        
            
        
    