# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:53:21 2018

@author: vcian
"""

"""If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?"""

# Euclid's formula for finding Pythagorean triples states that every triple is uniquely determined by integers m,n,k such that

# a = k(m^2-n^2)
# b = k(2mn)
# c = k(m^2 + n^2)
#
# Since 0 < a,b < c, it follows that
#
# c > 2
#
# m > n > 0 (as m,n < 0 yield the same triple as |m|,|n|)
#
# and
#
# k > 0. 
#
# The triple of smallest perimeter is (3,4,5), with perimeter 12, so k is bounded by 1000/12 < 84.
# Also, the largest possible size for b is 333, so n < (333/2)^.5 < 13. In summary:
#
# 0 < k 
# 0 < n < m < 1000^.5 < 32
#
# 

def gen_triple(k,m,n):
    a = k * (m**2 - n**2)
    b = k * 2 * m * n
    c = k * (m**2 + n**2)
    return (min(a,b),max(a,b),c)

perimeter_dict = {}
for m in range(2,32):
    for n in range(1,min(m,13)):
        for k in range(1,84):
            triple = gen_triple(k,m,n)
            perimeter = sum(triple)
            if perimeter <= 1000:
                if perimeter not in perimeter_dict:
                    perimeter_dict[perimeter] = [triple]
                else:
                    if not perimeter_dict[perimeter].count(triple):
                        perimeter_dict[perimeter].append(triple)

max_count = 0
max_p = 0
for p in perimeter_dict:
    if len(perimeter_dict[p]) > max_count:
        max_count = len(perimeter_dict[p])
        max_p = p