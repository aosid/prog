# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:47:27 2018

@author: vcian
"""

"""The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in
any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum
of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime."""

import primes

def all_cats(*slist):
    catlist = []
    for i in range(len(slist)):
        for j in range(0,i):
            catlist.extend((str(slist[i])+str(slist[j]),str(slist[j])+str(slist[i])))
    return catlist

if 'plist' not in dir():
    plist = primes.prime_less_than(10**4)
    plist = plist[1:1229]
    
def split_ab(ab):
    cands = []
    ab = str(ab)
    for i in range(1,len(ab)):
        if ab[i] == '0':
            continue
        a = ab[:i]
        b = ab[i:]
        if (int(a) in plist and int(b) in plist):
            if primes.is_prime(b + a):
                cand = [int(a),int(b)]
                cand.sort()
                if cand not in cands:
                    cands.append(cand)
    cands.sort()
    return cands

def vectorize(f):
    def helper(x,*y):
        if not y:
            raise TypeError('missing argument')
        else:
            for y_i in y:
                if not f(x,y_i):
                    return False
            return True
    return helper

def is_prime(n):
    n = int(n)
    if n in range(-1,2):
        return False
    if n == 2:
        return True
    for fact in plist:
        if n % fact == 0:
            return False
        if fact > n**.5:
            break
    return True

#@vectorize
def check_ab(a,b):
    return is_prime(str(a)+str(b)) and is_prime(str(b) + str(a))

#if "candlist" not in dir():
#    candlist = []
#    for p in plist:
#        cands = split_ab(p)
#        for cand in cands:
#            if cand not in candlist:
#                candlist.append(cand)
#    candlist.sort()
    
if "candlist" not in dir():
    candlist = []
    for i,p in enumerate(plist):
        for j in range(i):
            if check_ab(plist[j],p):
                candlist.append([plist[j],p])
    
def to_tree(candlist):
    candtree = {}
    for a,b in candlist:
        if a not in candtree:
            candtree[a] = set()
        candtree[a].add(b)
        if b not in candtree:
            candtree[b] = set()
        candtree[b].add(a)
    return candtree

if "candtree" not in dir():
    candtree = to_tree(candlist)
    
# don't run this
#newlist = []
#for x in candtree:
#    for y in candtree:
#        if y < x:
#            if check_ab(x,y):
#                newlist.append([x,y])
#
#for x,y in newlist:
#    candtree[x].add(y)
#    candtree[y].add(x)

#if "candlist" in dir():
#    newlist = []
#    for p in candtree:
#        for q in plist[plist.index(p)]:
#            if q not in candtree[p]:
#                if check_ab(p,q):
#                    newlist.append([q,p])
#    for q,p in newlist:
#        candtree[p].add(q)
#        if q not in candtree:
#            candtree[q] = set()
#        candtree[q].add(p)

# sorta slow
def find_trips(candtree):
    trips = []
    temp = []
    for x in candtree:
        for y in candtree[x]:
            for z in candtree[y]:
                if check_ab(x,z):
                    if z not in candtree:
                        temp.append([x,z])
                    trip = [x,y,z]
                    trip.sort()
                    if trip not in trips:
                        trips.append(trip)
    for x,z in temp:
        if z not in candtree:
            candtree[z] = set()
        candtree[z].add(x)
        candtree[x].add(z)
    trips.sort()
    return trips

def find_nextlets(nlets = None):
    if nlets == None:
        nlets = candlist
    nextlets = []
    for x,*y in nlets:
        for z in (candtree[x] - set(y)):
            if z in set.intersection(*[candtree[y_i] for y_i in y]):
                new = [x]
                new.extend(y)
                new.append(z)
                new.sort()
                if new not in nextlets:
                    nextlets.append(new)
    nextlets.sort()
    return nextlets

trips = find_nextlets()
quads = find_nextlets(trips)
quints = find_nextlets(quads)