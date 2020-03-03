# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:34:10 2019

@author: laksh
"""

for i in range (int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    cl=[]
    l2=[]
    c=0
    if n==1:
        print(*l)
        break
    for j in range (n-1):
        #print('j ',j)
        if l[j+1]==l[j]+1:
            c+=1
            up=l[j+1]
            #print('up ',up)
            lp=l[j-c+1]
            #print('lp ',lp)
            if j== n-2:
                #print('Yespppppppppppp')
                if c>1:
                    l2.append(lp)
                    #print('lp 1   ',lp)
                    l2.append('...')
                    l2.append(up)
                    #print('up   1 ',up)
                    #l2.append(',')
                    #print('l2  1 ',l2)
                    c=0
                elif c==1:
                    l2.append(lp)
                    #print('lp 2  ',lp)
                    l2.append(',')
                    l2.append(up)
                    #print('up   2 ',up)
                    #l2.append(',')
                    #print('l2   2 ',l2)
                    c=0
            #l2.append(l[j])
        else:
            if c>1:
                l2.append(lp)
                #print('lp 1   ',lp)
                
                l2.append('...')
                l2.append(up)
                #print('up   1 ',up)
                l2.append(',')
                #print('l2  1 ',l2)
                c=0
            elif c==1:
                l2.append(lp)
                #print('lp 2  ',lp)
                l2.append(',')
                l2.append(up)
                #print('up   2 ',up)
                l2.append(',')
                #print('l2   2 ',l2)
                c=0
            else:
                l2.append(l[j])
                l2.append(',')
                l2.append(l[j+1])
                #print('l2    3 ',l2)
    print(*l2)
    '''
    l3=[1,2,',','dfg']
    print(str(l3))
'''
                
                
                
                
            
    
    
    