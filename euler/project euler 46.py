# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:50:57 2018

@author: vcian
"""

"""It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"""

import primes

def is_square(n):
    return n**.5 == int(n**.5)

#  First odd composite.
i = 9

cont = False
while True:
    if primes.is_prime(i):
        i += 2
        continue
    print(i)
    plist = primes.prime_less_than(i)
    for p in plist:
        if is_square((i - p)/2):
            cont = True
            break
    if cont:
        cont = False
        i += 2
        continue
    break