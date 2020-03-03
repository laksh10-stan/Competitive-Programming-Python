# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:20:33 2019

@author: Lakshmendra Singh
"""

# cook your dish here
squares = [x**2 for x in range(1,33)][::-1]
print(squares)
T = int(input())
for __ in range(T):
    # N, K = map(int, input().split()) 
    N = int(input())
    count = 0
    while N>0:
        i=0
        while i<len(squares):
            x = squares[i]
            if x<=N:
                N -= x
                count += 1
            else:
                i+=1
            if N==0:
                break
    print(count)