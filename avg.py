# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:35:48 2019

@author: laksh
"""
from itertools import permutations
from itertools import combinations
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(float,input().split()))
    p=permutations(l,k)
    for i in list(p): 
        print (i)
    print("\n\n")
    c=combinations(l,k)
    avg=[]
    pi=[]
    
    for i in list(c): 
        print (i)
        print(sum(i)/len(i))
        avg.append(sum(i)/len(i))
        avr=sum(i)/len(i)
        pi.append(i)
    print(avg)
    print(pi)
    #(pi[0])
    ln=len(avg)
    print(ln)
    lt=[]
    #lt[0]=c[0]
    ak=avg[0]
    for i in range(1,ln):
        if avg[i]==ak:
            lt.append(pi[i])
        else:
            print(i)
    print(lt)
        
        
        
        
        
    
    
    