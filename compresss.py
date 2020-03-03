# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:05:02 2019

@author: laksh
"""

for i in range(int(input())):
    s=str(input())
    o=''
    y=0
    q=0
    for j in range(len(s)):
        y=q
        q=1
        for p in range(y,len(s)-1):
            if s[p+1]==s[p]:
                q+=1
                print(q)  
            else:
                o+str(s[p])
                o+str(q)
                break
        #s=s[2:]
    print(o)
            
            
    
    