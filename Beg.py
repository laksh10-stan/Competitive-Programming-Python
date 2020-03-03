# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:20:37 2019

@author: laksh
"""
t=int(input())
for i in range(t):
    s=int(input())
    if(s%2==0):
        al=0
        ev=0
        for j in range(s):
            a=j+1
            al+=a**2
            if(a%2==1):
                ev+=a**2
        al-=ev
        print(al)
    else:
        al=0
        for j in range(s):
            a=j+1
            if(a%2==1):
                al+=a**2
        print(al)
    
            
            
            
