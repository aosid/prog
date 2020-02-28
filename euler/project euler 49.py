# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:24:28 2018

@author: vcian
"""

"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii)
each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?"""

import primes
from itertools import permutations

plist = primes.prime_less_than(10**4)

for p in plist:
    if p > 1000:
        plist = plist[plist.index(p):]
        break

int_list = []
for p in plist:
    for q in plist[plist.index(p)+1:]:
        if tuple(str(q)) not in permutations(str(p)):
            continue
        r = q + (q - p)
        if r > 10**4:
            break
        if primes.is_prime(r):
            if tuple(str(r)) not in permutations(str(p)):
                continue
            int_list.append((p,q,r))