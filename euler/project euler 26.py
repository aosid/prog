# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:26:26 2018

@author: vcian
"""

"""Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

def rep_digits(d):
    rem_list = []
    dig_list = []
    r=1
    while r not in rem_list:
        rem_list.append(r)
        r = r*10
        while r < d:
            r = r*10
            dig_list.append(0)
        dig_list.append(r//d)
        r = r % d
        if r == 0:
            return []
    rep_ind = rem_list.index(r)
    return dig_list[rep_ind:]

max_rep = 0
max_d = 0
for i in range(1,1000):
    if len(rep_digits(i)) > max_rep:
        max_rep = len(rep_digits(i))
        max_d = i
        