# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:37:33 2019

@author: laksh
"""
def rev(p):
    return p[::-1]
from itertools import combinations
t=int(input())
for i in range (t):
    s=str(input())
    q,l0,r0,x0,y0,m=map(int,input().split())
    l=[]
    r=[]
    x=[]
    y=[]
    ans=0
    sm=0
    l.insert(0,l0)
    #print(l)
    r.insert(0,r0)
    #print(r)
    x.insert(0,x0)
    #print(x)
    y.insert(0,y0)
    #print(y)
    z=0
    for j in range(q):
        l.insert(j+1,1+(l[j]+ans)%len(s))
        #print(l[j+1])
        r.insert(j+1,1+(r[j]+ans)%len(s))
        #print(r[j+1])
        x.insert(j+1,1+(x[j]+ans)%m)
        #print(x[j+1])
        y.insert(j+1,1+(y[j]+ans)%len(s))
        #print(y[j+1])
        #print(l[j])
        #print(r[j+1])
        h=s[l[j+1]-1:r[j+1]]
        res = [h[x:y] for x, y in combinations(range(len(h) + 1), r = 2)]
        #print(res)
        #print(h)
        pal=[]
        #tem=''
        tem=[]
        for k in range(len(res)):
            tem.append(res[k])
            #print(tem)
            temp1=tem[k]
            temp2=rev(temp1)
            #print(temp1)
            #print(temp2)
            if temp1==temp2:
                pal.append(temp1)
        plt=[]
        #print(pal)
        #print(x[j+1])
        #print(y[j+1])
        for d in range (len(pal)):
            if ((len(pal[d])>x[j+1]-1) and (len(pal[d])<y[j+1]+1)):
                plt.append(pal[d])
        #print(plt)
        ans=len(plt)
        sm+=ans
        #print(ans)
        #print(sm)
        #print(s)
        z+=sm
    print(sm)
        
            
        
        #for k in range(len(h)):
            