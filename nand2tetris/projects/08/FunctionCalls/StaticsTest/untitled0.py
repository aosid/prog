# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:51:50 2019

@author: vcian
"""

class Stack:
    def __init__(self,*args):
        self.items = []
        for item in args:
            try:
                self.items.extend(item)
            except TypeError:
                self.items.append(item)
                
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return None
            
    def size(self):
        return len(self.items)
    
def is_balanced(expression):
    expression = str(expression)
    open_par_stack = Stack()
    
    openlist = '([{\'"'
    closelist= ')]}\'"'
    
    for char in expression:
        if char in openlist:
            open_par_stack.push(char)
        if char in closelist:
            if open_par_stack.peek() == openlist[closelist.index(char)]:
                open_par_stack.pop()
            else:
                return False
    return open_par_stack.isEmpty()

def dec_to_bin(n):
    rem_stack = Stack()
    q = n
    
    while q != 0:
        rem_stack.push(str(q % 2))
        q = q // 2
    if rem_stack.isEmpty():
        rem_stack.push('0')
        
    bin_list = []
    while not rem_stack.isEmpty():
        bin_list.append(rem_stack.pop())
    return "".join(bin_list)

def dec_to_base(n,b):
    rem_stack = Stack()
    q = n
    hex_dict = dict(zip(range(10,16),[chr(num) for num in range(65,71)]))
    
    while q != 0:
        if q % b > 9:
            rem_stack.push(hex_dict[q % b])
        else:
            rem_stack.push(str(q % b))
        q = q // b
    if rem_stack.isEmpty():
        rem_stack.push('0')
        
    bin_list = []
    while not rem_stack.isEmpty():
        bin_list.append(rem_stack.pop())
    return "".join(bin_list)