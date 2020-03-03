# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:22:44 2020

@author: laksh
"""
SX = 0
for i in range(int(input())):
    n = int(input())
    s=0
    loss = 0
    a = [[0 for i in range(4)] for j in range(4)]
    for j in range(n):
        m, T = map(str, input().split())
        t = int(T)
        #print(a)
        #print(m, t)
        if m == 'A' and t == 12:
            a[0][0] += 1
        elif m == 'A' and t == 3:
            a[0][1] += 1
        elif m == 'A' and t == 6:
            a[0][2] += 1
        elif m == 'A' and t == 9:
            a[0][3] += 1
        elif m == 'B' and t == 12:
            a[1][0] += 1
        elif m == 'B' and t == 3:
            a[1][1] += 1
        elif m == 'B' and t == 6:
            a[1][2] += 1
        elif m == 'B' and t == 9:
            a[1][3] += 1
        elif m == 'C' and t == 12:
            a[2][0] += 1
        elif m == 'C' and t == 3:
            a[2][1] += 1
        elif m == 'C' and t == 6:
            a[2][2] += 1
        elif m == 'C' and t == 9:
            a[2][3] += 1
        elif m == 'D' and t == 12:
            a[3][0] += 1
        elif m == 'D' and t == 3:
            a[3][1] += 1
        elif m == 'D' and t == 6:
            a[3][2] += 1
        elif m == 'D' and t == 9:
            a[3][3] += 1
    #print(a)
    mx = a[0][0]
    row = 0
    col = 0
    for k in range(4):
        for l in range(4):
            if(a[k][l] > mx):
                row = k
                col = l
                mx = a[k][l]
            #if(a[k][l])
    #print(mx)
    s += mx*100
    if mx == 0:
        loss += 1
    print(a[row].count(3))
    del a[row]
    del a[0][col]
    del a[1][col]
    del a[2][col]
    #print(a)
    
    mx = a[0][0]
    row = 0
    col = 0
    for k in range(3):
        for l in range(3):
            if(a[k][l] > mx):
                row = k
                col = l
                mx = a[k][l]
    #print(mx)
    s += mx*75
    if mx == 0:
        loss += 1
    del a[row]
    del a[0][col]
    del a[1][col]
    #print(a)
    
    mx = a[0][0]
    row = 0
    col = 0
    for k in range(2):
        for l in range(2):
            if(a[k][l] > mx):
                row = k
                col = l
                mx = a[k][l]
    #print(mx)
    s += mx*50
    if mx == 0:
        loss += 1
    del a[row]
    del a[0][col]
    #print(a)
    
    mx = a[0][0]
    row = 0
    col = 0
    for k in range(1):
        for l in range(1):
            if(a[k][l] > mx):
                row = k
                col = l
                mx = a[k][l]
    #print(mx)
    s += mx*25
    if mx == 0:
        loss += 1
    del a[row]
    s -= loss*100
    
    #print(a)
    
    print(s)
    SX += s
print(SX)
    
    #print (max_value(a))
    #print(max(map(lambda x: x[3], a)))
    #print(max(a[]))
    
    
    