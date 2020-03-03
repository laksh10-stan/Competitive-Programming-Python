# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:02:00 2019

@author: laksh
"""

t=int(input())
for i in range (t):
    n = int(input())
    l=list(map(int,input().split()))
    m=[]
    for j in range (len(l)):
        s=l[j]
        #print('j',j)
        #print('s',s)
        p=0
        for k in range(j+1,len(l)):
            #print('lk',l[k])
            #print('k',k)
            if s<l[k]:
                p+=1
                #print('p',p)
        m.append(p)
    print(*m,sep=' ')
        
    