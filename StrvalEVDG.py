# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:58:04 2019

@author: laksh
"""

for i in range (int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    #c=0
    #p=n
    #x=[0]*n
    #print(x)
    mas=0
    curr=0
    while(n>0):
        #z=0
        #print('curr=',curr)
        if curr>mas:
            mas=curr
            #print('mas=',mas)
        curr=0
        p=n
        #print(n)
        #x[n]=0
        #if max(x)>n:
            #print(n)
            #break
        if mas>n:
            break
        while (p>1):
            #print('p=',p)
            #print('n=',n)
            if l[p-2]%l[n-1]==0:
                #z+=1
                #x[n-1]+=1
                curr+=1
                #print('curr=',curr)
                #print(x)
            p-=1
            #print('curr=',curr)
            #print(x)
        n-=1
        #print(x)
        #print('curr=',curr)
        #print('mas=',mas)
        
    #print(x)
    #print(max(x))
    print(mas)
        