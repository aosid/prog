# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:38:43 2018

@author: vcian
"""

"""A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are 
listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

from math import factorial

def divider(r,n=9):
    r=r-1
    if factorial(n) < r:
        return None
    dig_choice = list(range(n+1))
    dig_list = []
    for i in range(n,-1,-1):
        i_fact = factorial(i)
        place = r // i_fact
        dig_list.append(dig_choice.pop(place))
        r = r % i_fact
    return dig_list
