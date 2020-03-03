# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 01:19:30 2019

@author: laksh
"""

for i in range(int(input())):
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=list(map(int,input().split()))
    flag11=0
    flag12=0
    flag21=0
    flag22=0
    flag31=0
    flag32=0
    flag41=0
    flag42=0
    flag51=0
    flag52=0
    flag61=0
    flag62=0
    if l1[0]>=l2[0] and l1[1]>=l2[1] and l1[2]>=l2[2] and l2[0]>=l3[0] and l2[1]>=l3[1] and l2[2]>=l3[2]:
        for i in range (3):
            if l1[i]>l2[i]:
                flag11=1
            if l2[i]>l3[i]:
                flag12=1
    if l1[0]>=l3[0] and l1[1]>=l3[1] and l1[2]>=l3[2] and l3[0]>=l2[0] and l3[1]>=l2[1] and l3[2]>=l2[2]:
        for i in range (3):
            if l1[i]>l3[i]:
                flag21=1
            if l3[i]>l2[i]:
                flag22=1
    if l2[0]>=l1[0] and l2[1]>=l1[1] and l2[2]>=l1[2] and l1[0]>=l3[0] and l1[1]>=l3[1] and l1[2]>=l3[2]:
        for i in range (3):
            if l2[i]>l1[i]:
                flag31=1
            if l1[i]>l3[i]:
                flag32=1
    if l2[0]>=l3[0] and l2[1]>=l3[1] and l2[2]>=l3[2] and l3[0]>=l1[0] and l3[1]>=l1[1] and l3[2]>=l1[2]:
        for i in range (3):
            if l2[i]>l3[i]:
                flag41=1
            if l3[i]>l1[i]:
                flag42=1
    if l3[0]>=l1[0] and l3[1]>=l1[1] and l3[2]>=l1[2] and l1[0]>=l2[0] and l1[1]>=l2[1] and l1[2]>=l2[2]:
        for i in range (3):
            if l3[i]>l1[i]:
                flag51=1
            if l1[i]>l2[i]:
                flag52=1
    if l3[0]>=l2[0] and l3[1]>=l2[1] and l3[2]>=l2[2] and l2[0]>=l1[0] and l2[1]>=l1[1] and l2[2]>=l1[2]:
        for i in range (3):
            if l3[i]>l2[i]:
                flag61=1
            if l2[i]>l1[i]:
                flag62=1
    if (flag11==1 and flag12==1) or (flag21==1 and flag22==1) or (flag31==1 and flag32==1) or (flag41==1 and flag42==1) or (flag51==1 and flag52==1) or(flag61==1 and flag62==1):
        print('yes')
    else:
        print('no')
                
    