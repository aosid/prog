# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:07:44 2018

@author: vcian
"""

"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator."""

#Notes:
#By the description of the problem, it seems likely that no digit can be 0.
#Generate fractions of the xy/zw from integers of the pattern xyzw:

from itertools import product

curious_list = []

digits = range(1,10)
fractions = list(product(digits,digits,digits,digits))

for frac in fractions:
    if frac[0] > frac[2]:
        continue
    if frac[0:2] == frac[2:4]:
        continue
    if (frac[0] == frac[3]):
        numer = (frac[0] * 10) + frac[1]
        denom = (frac[2] * 10) + frac[3]
        if numer/denom == frac[1]/frac[2]:
            curious_list.append([numer,denom])
    if (frac[1] == frac[2]):
        numer = (frac[0] * 10) + frac[1]
        denom = (frac[2] * 10) + frac[3]
        if numer/denom == frac[0]/frac[3]:
            curious_list.append([numer,denom])