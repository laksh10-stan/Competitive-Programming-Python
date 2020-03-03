# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:56:10 2020

@author: laksh
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def set_data(self, data):
        self.data = data
    def set_next(self, next):
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def has_next(self):
        return self.next != None
l = Node(1)
current = l
for i in range(2, 2021):
    current.set_next(Node(i))
    current = current.get_next()
current.set_next(l)
prev = current
current = l
n = int(input())
while l.has_next():
    for i in range(n):
        prev = current
        current = prev.get_next()
    if current == l:
        l = l.get_next()
    prev.set_next(current.get_next())
    current.set_data(None)
    current = prev.get_next()
print(l.get_data())