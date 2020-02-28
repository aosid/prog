# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:22:24 2018

@author: vcian
"""

"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

def divisors(n):
    divisors = set()
    for q in range(1,n):
        if n % q == 0:
            divisors.add(q)
    return divisors

def div_dict(n,memo={}):
    if n not in memo:
        if n in [0,1]:
            memo[n] = {0}
        else:
            memo[n] = divisors(n)
    return memo[n]

def div_sum(n):
    return sum(div_dict(n))

def find_friends(n):
    friend_list = []
    for i in range(1,n):
        if ((i != div_sum(i)) & (i == div_sum(div_sum(i)))):
            friend_list.append(i)
    return friend_list
