# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:29:24 2018

@author: vcian
"""

"""By replacing the 1st digit of the 2-digit number *3, it turns out that six
of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family."""
                           
import primes    
from itertools import combinations      

#how long of primes to consider
ndig = 6                                                      
                                                                
def insert_digs(n, k, digs):
    diglist = []
    nstr = str(n)
    kstr = str(k)
    j = 0
    for i in range(len(nstr) + len(digs)):
        if i in digs:
            diglist.append(kstr)
        else:
            diglist.append(nstr[j])
            j += 1
    return int("".join(diglist))

cdict = {}
for i in range(ndig):
    cdict[i] = list(combinations(range(ndig-1),i))

# must have at least 3 repeated digits
#final digit must be 1, 3, 7, or 9

for i in range(2,10**4):
    if i % 10 not in [1,3,7,9]:
        continue
    clen = ndig - len(str(i))
    for comb in cdict[clen]:
        compcount = 2
        lower = 0
        if 0 in comb:
            lower = 1
        for j in range(lower,10):
            if not primes.is_prime(insert_digs(i,j,comb)):
                compcount -= 1
                if compcount == 0: break
        if compcount == 0:
            continue
        else:
            for j in range(0,10):
                k = insert_digs(i,j,comb)
                print("{} is prime: {}".format(k,primes.is_prime(k)))
            raise Exception()