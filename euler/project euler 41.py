# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 13:46:04 2018

@author: vcian
"""

"""We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?"""

# All 8- and 9-digit pandigital numbers are divisible by 3, so we may exclude them. This
# is an immediately substantial improvement. We may also discard pandigitals ending
# in the numbers [0,2,4,5,6,8], as they are trivially non-prime.

from primes import is_prime
from itertools import permutations
from string import digits

pan_dig = []

for i in range(1,8):
    perms = permutations(digits[1:i+1])
    for perm in perms:
        if int(perm[-1]) in [0,2,4,5,6,8]:
            continue
        perm = "".join(perm)
        if is_prime(perm):
            pan_dig.append(perm)
