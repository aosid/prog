# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:27:13 2018

@author: vcian
"""

"""A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?"""

def dig_sum(n):
    dig_sum = 0
    while True:
        if not n:
            break
        dig_sum += n % 10
        n = n // 10
    return dig_sum

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def dig_root(n):
    dsum = dig_sum(n)
    if dsum < 10:
        return dsum
    return dig_root(dsum)

max_dig_sum = 0
for a in range(99,1,-1):
    for b in range(99,1,-1):
        dsum = dig_sum(a**b)
        if dsum > max_dig_sum:
            max_dig_sum = dsum