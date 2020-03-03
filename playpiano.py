# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:03:10 2019

@author: laksh
"""

t=int(input())
for i in range(t):
    s=str(input())
    l=len(s)
    f=1
    if(l%2==0):
        for k in range(0,l,2):
            if(l%2==0):
                if(s[k]==s[k+1]):
                    f=0
    else:
         for k in range(0,l):
             if(k%2==0):
                if(k==l-1):
                    if(s[k]==s[k-1]):
                        f=0   
                else:
                     if(s[k]==s[k+1]):
                        f=0                
    if(f==0):
        print("no")
    else:
        print("yes")
            
            
            
        