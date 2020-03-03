# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:31:26 2019

@author: laksh
"""

t=int(input())
for i in range (t):
    n=int(input())
    s=1
    r=1
    o=1
    l=1
    while n>=1:
        #r%=1000000007
        #r*=(s%1000000007**n%1000000007)
        #print(r)
        #r%=(s**n)
        #r*=(n**s)
        l=l*pow(n,s)%1000000007
        
        o=pow(o*pow(n,s),1,1000000007)
        
        
        #print(r)
        #r%=1000000007
        #o*=r
        #print(o)
        s+=1
        n-=1
    #print(r)
    print(l)
    print(o)
        
        
        