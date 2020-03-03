# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:13:37 2019

@author: laksh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:06:40 2019

@author: laksh
"""

t=int(input())
for i in range (t):
    n=int(input())
    l=[[]]
    for j in range(n):
        l[j][]=list(map(int,input().split()))
        print(l[j])
        #c,a,b=map(int,input().split())
        if(l[j][0]==1):
            print("YES")
        elif(l[j][0]==2):
            if(l[j][1]==l[j][2]):
                print("YES")
            if(j==0):
                print("NO")
            elif(j!=0):
                if(min(l[j])<max(l[j-1])):
                    print("YES")
        
            
            