# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:05:09 2018

@author: vcian
"""

"""The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000."""


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def modexp(a,b,m):
    # calculate a^b mod m.
    if a in [0,1]:
        return a
    if b == 1:
        return a % m
    for i in [a,b,m]:
        if type(i) != int:
            raise TypeError("terms must be integers.")
        if i <= 0:
            raise ValueError("terms must be non-negative. a = {}, b = {}, m = {}".format(a,b,m))
    if a >= m:
        return modexp(a % m,b,m)
    b_hat = 1
    prod = 1
    while True:
        prod *= a
        if prod >= m:
            break
        if b_hat == b:
            return a**b
        b_hat += 1
    # a_hat = a^b_hat mod m
    a_hat = prod % m
    
    l = b // b_hat
    k = b % b_hat
    
    # note that b = l * b_hat + k. then
    # k = b - (l * b_hat), so
    # if this all worked out, then
    # a^b = (a^b_hat)^l * a^k
    #     =  a_hat ^ l  * a^k
    
    return (modexp(a_hat,l,m) * a**k) % m

acc_sum = 0
for i in range(1,1001):
    acc_sum += modexp(i,i,10**10)
    acc_sum = acc_sum % 10**10
print(acc_sum)