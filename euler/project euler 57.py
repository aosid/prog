# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:41:17 2018

@author: vcian
"""

"""It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion,
1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?"""

import sys
from fractions import frac

sys.path.append('C:\\Users\\vcian\\.spyder-py3')

def n_digits(n):
    i = 0
    while True:
        if n // 10**i == 0:
            return i
        i += 1

#def cont_iter(n):
#    if n == 0:
#        return frac(1,1)
#    curr_b = 2
#    for i in range(n-1):
#        curr_b = 2 + frac(1,curr_b)
#    return 1 + frac(1,curr_b)
#        
#count = 0
#for i in range(1001):
#    expansion = cont_iter(i)
#    if n_digits(expansion.numer) > n_digits(expansion.denom):
#        count += 1
        
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def memo_iter(n):
    if n == 0:
        return frac(1,1)
    return 1 + frac(1,1+memo_iter(n-1))

count = 0
for i in range(1001):
    expansion = memo_iter(i)
    if n_digits(expansion.numer) > n_digits(expansion.denom):
        count += 1