# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:36:48 2019

@author: laksh
"""

for i in range(int(input())):
    a,m=map(int,input().split())
    #z=q
    l=[]
    c=0
    q=m//a
    r=m%a
    while(q>0):
        #print('q',q)
        #print('r',r)
        if(r!=0):
            if(q%r==0 and m==(a*q)+r ):
                c+=1
                #print('c',c)
                l.append(q)
                #print('l',l)
                q-=1
                r=m%q
                
            else:
                q-=1
                r=m%q
        else:
            if(m==(a*q)+q):
                c+=1
                l.append(q)
                q-=1
            else:
                q-=1
            '''
            if(q%r==0 and m==(a*q)+r ):
                c+=1
                print('c',c)
                l.append(q)
                print('l',l)
                q-=1
                r=m%q
                
            else:
                q-=1
                r=m%q
            '''
            
    print(c)
    l=l[::-1]
    print(*l)
    
            
            
            
            
            
    
    