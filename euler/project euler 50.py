# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:50:07 2018

@author: vcian
"""

"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?"""

import primes

plist = primes.prime_less_than(1000000)

max_terms = 1
stop = len(plist)
for i in range(stop):
    j = i+max_terms
    if j > stop:
        break
    accsum = sum(plist[i:j])
    while True:
        if j > stop:
            break
        if accsum > 10**6:
            break
        if (j-i > max_terms) and primes.is_prime(accsum):
            print("the prime {} is the sum of the {} primes from {} to {}.".format(accsum,j-i,plist[i],plist[j]))
            max_terms = j-i
        accsum += plist[j]
        j += 1