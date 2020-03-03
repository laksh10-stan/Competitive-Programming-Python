# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:06:12 2019

@author: laksh
"""
def redArr(l,k):
    y=0
    g=len(l)
    #print(g)
    z=(g//k+g%k)
    #print(z)
    m=[]
    for u in range (z):
        if(g%k==0):
            s=0
            for i in range (k):
                s+=l[y]
                y+=1
            m.insert(u,s)
        else:
            s=0
            if(u==z-1):
                for i in range (k-1):
                    s+=l[y]
                    y+=1
            else:
                for i in range (k):
                    s+=l[y]
                    y+=1
            m.insert(u,s)
    if(len(m)>=k):
        l=redArr(m,k)
    else:
        print(m)
   
t=int(input())
for _ in range (t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l1=redArr(l,k)

        