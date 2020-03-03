# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:58:04 2019

@author: laksh
"""

for i in range (int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    e=[]
    for g in l:
        if g%2==0:
            e.append(g)
    mas=0
    curr=0
    mas2=0
    curr2=0
    ev=len(e)
    while(n>0):
        #print('curr=',curr)
        if curr>mas:
                mas=curr
        if mas>=n:
                break
        curr=0
        p=n
        if l[n-1]%2!=0:
            #print('YES')
            #print(l[n-1])
            #print(n)
            #curr=0
            #p=n
            #print('mas=',mas)
            while (p>1):
                #print('p=',p)
                #print('n=',n)
                if l[p-2]%l[n-1]==0:
                    curr+=1
                    #print('curr=',curr)
                p-=1
                #print('curr=',curr)
        n-=1
    while(ev>0):
        #print('curr=',curr)
        if curr2>mas2:
            mas2=curr2
        if mas2>=ev:
            break
        curr2=0
        q=ev
        #print('YES')
        #print(e[ev-1])
                #print(n)
                #curr=0
                #p=n
                #print('mas=',mas)
        while (q>1):
                    #print('p=',p)
                    #print('n=',n)
            if e[q-2]%e[ev-1]==0:
                curr2+=1
                        #print('curr=',curr)
            q-=1
                    #print('curr=',curr)
        ev-=1
        #print('curr=',curr)
        #print('mas=',mas)
    #print(mas2, 'mas2')
    #print(mas, 'mas')
    print(max(mas,mas2))
        