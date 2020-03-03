# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:42:21 2019

@author: laksh
"""

for i in range(int(input())):
    n = int(input())
    l=[]
    if n == 1:
        print('1')
    else:
        for j in range(n):
            if j == 0:
                l.append(0)
            else:
                if l.count(l[-1]) == 1:
                    l.append(0)
                else:
                    l2 = l[::-1]
                    l2.pop(0)
                    l.append(l2.index(l[-1])+1)
        print(l.count(l[-1]))
                
                
                
                
            
        
        
        
        