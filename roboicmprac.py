# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:02:16 2019

@author: laksh
"""
for i in range (int(input())):
    s=input()
    #for j in range(len(l)):
    #print(s)
    ln = []
    idx=[]
    lp=[]
    p=0
    for el in s:
        try:
            ln.append(int(el))
            lp.append(int(el))
            idx.append(p)
        except ValueError:
            lp.append(10)
            pass
        p+=1
    if len(ln)==(0 or 1):
        print('safe')
    else:
        c=0
        for k in range (len(lp)):
            if lp[k]!=10:
                t=lp[k]
                continue
            
    print(idx)    
    print(ln)
    print(lp)
    
    #for j in range(len(l)):
        
        
        
