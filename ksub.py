# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:16:01 2019

@author: laksh
"""

from itertools import chain, combinations

def subsets(arr):
    """ Note this only returns non empty subsets of arr"""
    return chain(*[combinations(arr,i + 1) for i,a in enumerate(arr)])

def k_subset(arr, k):
    s_arr = sorted(arr)
    return set([(i) for i in combinations(subsets(arr),k) 
               if sorted(chain(*i)) == s_arr])


print (k_subset([1,2,3,4],2))