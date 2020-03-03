# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 22:05:41 2019

@author: laksh
"""
#import itertools
from itertools import repeat
t=int(input())
for i in range (t):
    a,b,c=map(int,input().split())
    l=[]
    l.extend(repeat(1,a))
    l.extend(repeat(2,b))
    l.extend(repeat(3,c))
    #print(l)
    if a%2==0 and b%2==0 and c%2==0:
        print('YES')
    elif a%2==0 and b%2==0 and c%2==1:
        print('NO')
    elif a%2==0 and b%2==1 and c%2==0:
        if (a!=0 or b%3==0):
            print('YES')
        else:
            print('NO')
    elif a%2==0 and b%2==1 and c%2==1:
        print('NO')
    elif a%2==1 and b%2==0 and c%2==0:
        print('NO')
    elif a%2==1 and b%2==0 and c%2==1:
        if (a%3==0 and c!=0):
            print('YES')
        elif(a%3==2 and b%3==1 and c>1):
            print('YES')
        else:
            print('NO')
    elif a%2==1 and b%2==1 and c%2==0:
        print('NO')
    else:
        if(b%3==0 or (a+b)%2==0):
            print('YES')
        else:
            print('NO')
    
    
        