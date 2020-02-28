# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:19:37 2018

@author: vcian
"""

"""The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?"""

from primes import factorize

n = 1
# Given lower bound.

#while True:
#    cont = False
#    for i in range(4):
#        if len(factorize(n+i)) < 4:
#            cont = True
#    if cont:
#        n += 1
#        continue
#    for i in range(4):
#        print("{}: {}".format((n+i),factorize(n+i)))
#    break

while True:
    cont = False
    for i in range(4):
        if len(factorize(n+i)) < 4:
            cont = True
    if cont:
        n += 1
        continue
    for i in range(4):
        print("{}: {}".format((n+i),factorize(n+i)))
    break