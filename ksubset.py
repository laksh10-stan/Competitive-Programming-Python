# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:08:36 2019

@author: laksh
"""
import copy
arr = [1,2,3,4]

def t(k,accum,index):
    print (accum,k)
    if index == len(arr):
        if(k==0):
            return accum
        else:
            return []

    element = arr[index]
    result = []

    for set_i in range(len(accum)):
        if k>0:
            clone_new = copy.deepcopy(accum)
            clone_new[set_i].append([element])
            result.extend( t(k-1,clone_new,index+1) )

        for elem_i in range(len(accum[set_i])):
            clone_new = copy.deepcopy(accum)
            clone_new[set_i][elem_i].append(element)
            result.extend( t(k,clone_new,index+1) )

    return result

print (t(2,[[]],0))