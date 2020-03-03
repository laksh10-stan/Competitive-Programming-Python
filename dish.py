# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:29:00 2019

@author: laksh
"""

t=int(input())
for i in range(t):
    s=int(input())
    l=[]
    a=''
    for j in range(s):
        l.append(str(input()))
        a+=l[j]
    #print(l)   
    #print(a)
    n=len(a)
    #print(n)
    z=0
    k=0
    print(a)
    c,o,d,e,h,f=0,0,0,0,0,0
    while(a[k]!='\0'):
        if(a[k]=='c' or a[k]=='o' or a[k]=='d' or a[k]=='e' or a[k]=='h' or a[k]=='f'):
            if(a[k]=='c'):
                c+=1
                a=a[:k]+a[k+1:]
                #a.replace('c','',1)
                print(a)
            if(a[k]=='o'):
                o+=1
                a.replace('o','',1)
            if(a[k]=='d'):
                d+=1
                a.replace('d','',1)
            if(a[k]=='e'):
                e+=1
                a.replace('e','',1)
            if(a[k]=='h'):
                h+=1
                a.replace('h','',1)
            if(a[k]=='f'):
                f+=1
                a.replace('f','',1)
        if (c==2 and o==1 and d==1 and e==2 and h==1 and f==1):
            z+=1
            print(a)
            c,o,d,e,h,f=0,0,0,0,0,0
        k+=1
    print(z)
        