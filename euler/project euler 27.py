# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:26:25 2018

@author: vcian
"""

"""Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

Find the product of the coefficients, a and b, for the quadratic expression that 
produces the maximum number of primes for consecutive values of n, starting with 
n=0."""
import primes

#|a| < 1000
a_list = list(range(-999,1000))

#|b| <= 1000, must be prime
temp_list = prime_less_than(1000)
b_list = []
for b in temp_list:
    b_list.append(b)
    b_list.append(-b)

max_primes = 1
max_pair = (0,0)

for a in a_list:
    for b in b_list:
        n = 0
        while True:
            p = abs(n**2 + a*n + b)
            if not is_prime(p):
                break
            n += 1
        if max_primes < (n + 1):
            max_primes = (n + 1)
            max_pair = (a,b)

print("Maximum number of primes: " + str(max_primes))
print("Max pair: " + str(max_pair))
print("a * b = " + str(max_pair[0] * max_pair[1]))