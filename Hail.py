# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:33:41 2019

@author: laksh
"""
from collections import counter
t=int(input())
for i in range(t):
    k=int(input())
    s=str(input())
    i,j=0,0
    n=len(s)
    ulk=0
    for i in range(1,len(s)+1):
        for j in range(1,len(s)+1):
            if(k<=j-i+1) and (i>=1) and (j<=len(s)):
                if(i<=j):
                    print(i,j)
                    temp=''
                    lop=list(s)
                    del lop[i-1:j]
                    temp="".join(lop)
                    print(temp)
                    all_freq = {}
                    count=0
                    num=0
                    res=counter(temp)
                    for m in temp: 
                        if m in all_freq: 
                            all_freq[m] += 1
                        else: 
                            all_freq[m] = 1
                            num+=1
                    print(all_freq)
                    for z in all_freq:
                        if z%2==0:
                            count+=1
                    if count==num:
                        ulk+=1
                        
                elif(j<i):
                    print(i,j)
                    temp=''
                    lop=list(s)
                    del lop[j-1:i]
                    temp="".join(lop)
                    print(temp)
                else:
                    temp=''
                    #lop=list(s)
                    #lop.pop(q-1)
                    #temp="".join(lop)
                    #temp=s[:i]+s[j:]
                    print(temp='z')
    print(ulk)
                
        
    
    
    