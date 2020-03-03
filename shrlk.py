# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:01:50 2019

@author: laksh
"""

t=int(input())
ins=int(input())
l=[]
s=''
while(ins>0):
    l.append(ins%10)
    ins=ins//10
l=l[::-1]
for i in range(len(l)):
    if l[i] == 1:
        s+='a'
    elif l[i]== 2:
        s+='bb'
    elif l[i]== 3:
        s+='ab'
    if l[i]==4:
        li=list(char for char in s)
        print(li)
        #k=s.replace('a','b')
        #s=k.replace('b','a')
        for j in range(len(li)):
            if li[j]=='a':
                li[j]='b'
            if li[j]=='b':
                li[j]='a'
        print(li)
        s=''
        s=s.join(li)
                
print(s)
            
            
        
        
    