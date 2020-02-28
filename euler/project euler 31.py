# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:02:33 2018

@author: vcian
"""

"""In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

How many different ways can £2 be made using any number of coins?"""

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def solutions_with_order(total):
    
    #This returns the number of solutions if the order of selection of coins matters. Whoops.
    
    if type(total) != int:
        raise TypeError("total must be an int.")
    if total < 0:
        raise ValueError("total must be at least 0.")
    global vals
    if total in [0,1]:
        return 1
    else:
        n_solutions = 0
        for val in vals:
            if val <= total:
                n_solutions += solutions_with_order(total-val)
        return n_solutions
     
        
def solutions(total,vals=[1,2,5,10,20,50,100,200]):    
    
    #After a coin is chosen, subsequent coins must be of equal or lesser value.
    
    if type(total) != int:
        raise TypeError("total must be an int.")
    if total < 0:
        raise ValueError("total must be at least 0.")
    if total in [0,1]:
        return 1
    else:
        n_solutions = 0
        for val in vals:
            if total - val >= 0:
                largest_coin_index = vals.index(val)
                n_solutions += solutions(total-val,vals[:largest_coin_index + 1])
        return n_solutions
    
    
def memoize_mult(f):
    memo = {}
    def helper(x,y=8):
        if x not in memo:
            memo[x] = dict()
            memo[x][y] = f(x,y)
        if y not in memo[x]:
            memo[x][y] = f(x,y)
        return memo[x][y]
    return helper    

vals = [1,2,5,10,20,50,100,200]

@memoize_mult
def solutions_memo(total,val_ind = 8):    
    
    #Attempt to memoize the previous function for speed.
    
    global vals
    
    if type(total) != int:
        raise TypeError("total must be an int.")
    if total < 0:
        raise ValueError("total must be at least 0.")
    if total in [0,1]:
        return 1
    else:
        n_solutions = 0
        for val in vals[:val_ind]:
            if total - val >= 0:
                largest_coin_index = vals.index(val)
                n_solutions += solutions_memo(total-val,largest_coin_index + 1)
        return n_solutions