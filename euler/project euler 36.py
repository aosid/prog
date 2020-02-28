# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:19:53 2018

@author: vcian
"""

"""The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""

def is_pal(n):
    n_str = str(n)
    rev = []
    for char in n_str:
        rev.insert(0,char)
    r_str = "".join(rev)
    if r_str == n_str:
        return True
    return False

def make_pal(n):
    n_str = str(n)
    rev = []
    for char in n_str:
        rev.insert(0,char)
    r_str = "".join(rev)
    return int(n_str + r_str)

pal_list = [make_pal(n) for n in range(1,1000)]

def make_odd_pal(n,m):
    n_str = str(n)
    rev = []
    for char in n_str:
        rev.insert(0,char)
    r_str = "".join(rev)
    return int(n_str + str(m) + r_str)

for i in range(10):
    if i != 0:
        pal_list.append(i)
    for j in range(1,100):
        pal_list.append(make_odd_pal(j,i))

def make_bin(n):
    n = int(n)
    i = 0
    while 2**i < n:
        i += 1

    bit_list = []
    for j in range(i,-1,-1):
        if n // 2**j:
            bit_list.append("1")
            n = n % 2**j
        else:
            bit_list.append("0")
    return "".join(bit_list).lstrip("0")

double_pal = []

for n in pal_list:
    if is_pal(make_bin(n)):
        double_pal.append(n)
        
double_pal.sort()