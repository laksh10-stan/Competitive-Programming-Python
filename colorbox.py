# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:26:33 2019

@author: laksh
"""

for i in range(int(input())):
    n,m = map(int,input().split())
    l=list(map(int,input().split()))
    nl = [l[p * m:(p + 1) * m] for p in range((len(l) + m - 1) // m )]  
    d = 10**10
    print(nl)
    #nl = list(map (lambda x: l[3*x:(x+1)*3], range (3)))
    for j in range(len(nl)-1):
        cmax = max(nl[j])
        #print('cmax',cmax)
        cmin = min(nl[j])
        #print('cmin',cmin)
        if d > cmax - cmin:
            d = cmax - cmin
        #d = cmax - cmin
        #print(cmax, cmin)
        #print(d)
        for k in range(len(nl[j])):
            tl = nl[j].copy()
            #print(nl[j])
            print('tl',tl)
            del tl[k]
            #print('tlshort',tl)
            for h in range(len(nl)):
                #print('lastl',len(nl[-1]))
                if h != j:
                    if h == len(nl)-1 and k < len(nl[-1]):
                        nmax = max(nl[h][k],max(tl))
                        #print('nmax',nmax)
                        nmin = min(nl[h][k],min(tl))
                        #print('nmim',nmin)
                        newd = nmax - nmin
                        #print('newd',newd)
                        if d > newd:
                            d = newd
    print(d)
                
            
        
    
    
    