# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:54:59 2018

@author: vcian
"""

"""There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	n! / r!(n−r)!

where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?"""

from math import factorial

total = 0
for n in range(1,101):
    for r in range(0,n):
        if factorial(n) / (factorial(r) * factorial(n - r)) > 10**6:
            print("{}C{} = {}".format(n,r,factorial(n) / (factorial(r) * factorial(n - r))))
            total += n - 2*r + 1
            break

#for n in range(1,101):
#    for r in range(0,n):
#        if factorial(n) / (factorial(r) * factorial(n - r)) > 10**6:
#            total += 1
            