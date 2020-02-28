# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:02:58 2018

@author: vcian
"""

"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""

from math import factorial

fact_list = []
for i in range(0,10):
    fact_list.append(factorial(i))

curious_list = []

#Note: 9! = 362880.
#Since 9! * 8 < 10^7, we need only check up to 10^7-1.
#This bound can probably be improved.
upper = 10**7 - 1

for i in range(2,upper):
    print(i)
    dig_list = [int(dig) for dig in str(i)]
    
    if fact_list[max(dig_list)] > i:
        continue
    
    fact_sum = 0
    for dig in dig_list:
        fact_sum += fact_list[dig]
    
    if fact_sum == i:
        curious_list.append(i)