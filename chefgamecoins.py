# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:47:37 2019

@author: laksh
"""

for i in range(int(input())):
    n = int(input())
    l=[]
    #ls=[]
    for j in range(n):
        l.append(list(map(int, input().split())))
        #ls.append(l[j][0])
        del l[j][0]
    c=0
    lmid=[]
    for j in range(n):
        if len(l[j])%2 == 0:
            c+=sum(l[j][0:len(l[j])//2])
        else:
            c+=sum(l[j][0:len(l[j])//2])
            lmid.append(l[j][(len(l[j])//2)])
    lmidsorted = sorted(lmid, reverse = True)
    for q in range(0, len(lmidsorted), 2):
        c+=lmidsorted[q]
    print(c)            
            
        
        
    
    