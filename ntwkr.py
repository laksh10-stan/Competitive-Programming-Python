# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 23:08:38 2019

@author: laksh
"""
import itertools
#from itertools import permutations 
#from itertools import combinations
#from itertools import product
t=int(input())
for i in range (t):
    n,m=map(int,input().split())
    ln=[]
    for j in range (n):
        ln.append(j+1)
    print(ln)
    net = list(itertools.combinations_with_replacement(ln, 2))
    print(net)
    print(len(net))
    if n==1:
        if m==0:
            print(0)
            break
        elif m==1:
            print (1)
            break
        else:
            print(-1)
            break
    elif n==2:
        if m<n-1 or m>(((n*(n-1))/2)+n):
            print(-1)
        elif m==1:
            print(1)
            break
        else:
            print(2)
            break
    else:
        if m<n-1 or m>(((n*(n-1))/2)+n):
            print(-1)
        else:
            for dc in range (2,n+1):
                w=[]
                count=0
                for j in range (len(net)):
                    if net[j][1] == net[j][0] + 1 or net[j][1] == net[j][0] + n-1:
                        count+=1
                    if m==count:
                        print(dc)
                        break
                print(count)
    '''for k in range(n):
        for l in range(n):
           if l4[k][l]:
               l3.append((l+1,k+1))
    '''