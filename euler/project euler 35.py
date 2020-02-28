# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:26:03 2018

@author: vcian
"""

"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""

import primes

plist = primes.prime_less_than(10**6)
cplist = []

def rotate(n):
    len_n = len(str(n))
    rotations = []
    for i in range(len_n):
        rotations.append(n)
        n = (10**(len_n)*(n%10)+n)//10
    return rotations

for p in plist:
    p_rots = rotate(p)
    try:
        for p in p_rots:
            if not primes.is_prime(p):
                raise Exception
    except:
        continue
    cplist.append(p)