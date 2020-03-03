# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:55:55 2019

@author: laksh
"""

t=int(input())
for i in range (t):
    points = dict()
    gd = dict()
    for j in range (2):
        l = list(map(str,input().split()))
        if int(l[1]) > int(l[3]):
            if l[0] in points:
                points[l[0]] += 3
            else:
                points[l[0]] = 3
        elif int(l[1]) < int(l[3]):
            if l[4] in points:
                points[l[4]] += 3
            else:
                points[l[4]] = 3
        else:
            if  l[1] in points:
                points[l[0]] += 1
            else:
                points[l[0]] = 1
            if l[3] in points:
                points[l[4]] += 1
            else:
                points[l[4]] = 1
        if int(l[1]) > int(l[3]):
            if l[0] in gd:
                gd[l[0]] += int(l[1])-int(l[3])
            else:
                gd[l[0]] = int(l[1])-int(l[3])
        elif int(l[1]) < int(l[3]):
            if l[4] in gd:
                gd[l[4]] += int(l[3]) - int(l[1])
            else:
                gd[l[4]] = int(l[3]) - int(l[1])
        else:
            if l[0] in gd:
                gd[l[0]] += int(l[1])-int(l[3])
            else:
                gd[l[0]] = int(l[1])-int(l[3])
            if l[4] in gd:
                gd[l[4]] += int(l[3]) - int(l[1])
            else:
                gd[l[4]] = int(l[3]) - int(l[1])


print(points)
print(gd)       
        
    
    