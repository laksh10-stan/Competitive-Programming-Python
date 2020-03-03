# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:28:13 2019

@author: laksh
"""

for i in range(int(input())):
    n = int(input())
    l=[0,0,0,0,0,0,0,0,0,0]
    l2=[]
    s1="0000000000"
    s2=""
    for j in range(n):
        #l2=list(map(int, input().split()))
        #l2=l2^l
        #l=l2
        s2=str(input())
        print('s2',s2)
        print(type(s1))
        s2=int(s2)^int(s1)
        print('s2',s2)
        print(type(s1))
        s1=str(s2)
        print(type(s1))
        print('s1',s1)
    print(s1.count("1"))
        
        
        
        