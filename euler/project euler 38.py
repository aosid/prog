# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:25:38 2018

@author: vcian
"""

"""Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?"""

#Notes: The integer can have at most four digits.

from string import digits

def array_mult(n):
    char_set = set()
    compare_set = set(digits)
    compare_set.remove("0")
    i = 1
    while True:
        if char_set == compare_set:
            return (i-1)
        nstr = str(n * i)
        for char in nstr:
            if char in char_set:
                return -1
            char_set.add(char)
        i += 1

int_n = {}
for i in range(10000):
    n = array_mult(i)
    if n == -1:
        continue
    int_n[i] = n