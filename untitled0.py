# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:25:17 2020

@author: laksh
"""

class Check(sum, n):
    def _init_(self, sum, n):
        self.sum = sum
        self.n = n
        self.d = []
        def put(j, x):
            for i in d:
                if i[self.n]+x<self.sum:
                    i[j] = x
                    i[self.n] += x
                elif i[self.n]+x==sum:
                    i[j] = x
                    return i
            self.d.append({j:x, self.n:x})
            return {}

sum, n = map(int, input().split ())
l = list(map(int, input ().split ()))
c = Check (sum, n)
for i in range(n):
    d = c.put(i, l[i])
    if d!={}:
        break
l = d.keys()
print (len(l))
for i in l:
    print(i, endl=" ")