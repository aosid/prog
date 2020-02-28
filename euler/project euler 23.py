# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:51:47 2018

@author: vcian
"""

"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as 
the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater 
than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced 
any further by analysis even though it is known that the greatest number that cannot be expressed as the sum
of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

from math import ceil as ceil

def divisors(n):
    div_list = []
    for i in range(1,ceil((n/2)+1)):
        if n % i == 0:
            div_list.append(i)
    return div_list

upper = 28123
ab_nums = []

for i in range(upper):
    if sum(divisors(i)) > i:
        ab_nums.append(i)

def sum_possible(n,summands):
    for a in summands:
        b = n-a
        try:
            summands.index(b)
            return True
        except ValueError:
            continue
    return False

sum_poss = set()
for i in range(len(ab_nums)):
    for j in range(i,len(ab_nums)):
        sum_poss.add(ab_nums[i]+ab_nums[j])
sum_poss = list(sum_poss)        

sum_not_poss = list(range(1,upper))
for i in sum_poss:
    if i == upper:
        break
    sum_not_poss.remove(i)