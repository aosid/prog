# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:43:41 2018

@author: vcian
"""

"""Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

four_list = []
five_list = []

for n in range(10000000):
    nstr = str(n)
    dig_list = list(nstr)
    for i in range(len(dig_list)):
        dig_list[i] = int(dig_list[i])
    
#    sum_4 = 0
    sum_5 = 0
    for dig in dig_list:
        dig_4 = dig**4
#        sum_4 += dig_4
        sum_5 += dig_4 * dig

#    if n == sum_4:
#        four_list.append(n)
    if n == sum_5:
        five_list.append(n)        