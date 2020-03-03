# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:33:20 2019

@author: laksh
"""
from itertools import permutations 
from itertools import combinations
from itertools import product
l=[1,2,1,3,4,5,6,2,3,4,5,6]
l2=[1,2,3,4,5,6]
print(len(list(combinations(l,2))))
print (list(combinations(l,2)))
print(len(list(combinations(l2,2))))
print (list(combinations(l2,2)))
all_list = [[1, 2,3, 4,5,6], [1, 2,3, 4,5,6] ] 
  
# printing lists  
print ("The original lists are : " + str(all_list))
res = list(product(*all_list)) 
  
# printing result 
print ("All possible permutations are : " +  str(res)) 
print(list(product(range(5),repeat=2)))
print(len(list(product(range(5),repeat=2))))