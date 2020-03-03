# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:00:21 2020

@author: laksh
"""
for i in range(int(input())):
    n, p = map(int, input().split())
    d = list(map(int, input().split()))
    l = []
    q = []
    tt = -44
    yy = -23
    if 2 in d and p%2 != 0:
        break
    for z in range(len(d)):
        
        if p%d[z] == 0:
            l.append(0)
            q.append(0)
        else:
            if d[z]>p:
                l.append(d[z] - p)
                if d[z] - p == 1:
                    tt = z
                    yy = 1
                    print('yy1', yy, 'tt1' , tt)
                    break
                q.append(1)
            else:
                l.append(d[z] - p%d[z])
                if d[z] - p%d[z] == 1:
                    tt = z
                    yy = p//d[z] + 1
                    print('yy2', yy, 'tt2' , tt)
                #print(p, " " , d[z])
                q.append(p//d[z])
    #while max(l) > min(d):
        
                
        '''
    for j in range(len(d)):
        if p%d[j] == 0:
            l[j] = 0
        else:
            l[j] = 1 
            '''
    print(l)
    print(q)
    
    
    
    
