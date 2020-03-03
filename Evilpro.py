# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:35:06 2019

@author: laksh
"""

for i in range(int(input())):
    s=str(input())
    ls=list(s)
    for j in range(len(ls)):
        l=j
        r=l
        for k in range(len(ls)-j):
            o=ls
            print(o)
            if(r!=len(ls)):
                for x in range(l,r+1):
                    if ls[x]==0:
                        #print('wert')
                        o[x]==
                    else:
                        #o[r]='0'
                        #print('wert')
                        o.insert(x,1)
                        

                print(o)
                r+=1
            else:
                 for x in s[l:]:
                    if x=='0':
                        o[r]='1'
                    else:
                        o[r]='0'     
                 print(o)
                 r+=1
            k+=1
                
            
            
            