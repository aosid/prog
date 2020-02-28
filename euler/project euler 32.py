# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:30:27 2018

@author: vcian
"""

"""We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 
pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital."""

#Notes: The only possible digit patterns are
# _ x _ _ _ _ = _ _ _ _
# _ _ x _ _ _ = _ _ _ _
#
#The final digit of each factor cannot be 1.

from itertools import permutations

possible_strings = list(permutations(range(1,10)))
correct_strings = set()

def catted(digits):
    catted = ""
    for digit in digits:
        catted += str(digit)
    return int(catted)

for string in possible_strings:
    if string[4] == 1:
        continue
    if string[0] != 1:
        if string[0] * catted(string[1:5]) == catted(string[5:]):
            correct_strings.add(catted(string[5:]))
    if string[1] != 1:
        if catted(string[0:2]) * catted(string[2:5]) == catted(string[5:]):
            correct_strings.add(catted(string[5:]))
