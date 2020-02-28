# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:14:12 2018

@author: vcian
"""

"""Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?"""

#def draw_spiral(n):
#    #Draws a sequence of natural numbers in an n by n spiral, starting with 1 in the center and moving right then clockwise.
#    
#    if (n < 0) or (n % 2 != 1):
#        raise Exception("n must be an odd natural number.")
#    
#    #Number of rings, not counting the center.    
#    n_rings = (n-1) / 2
#    
#    #New grid.
#    grid = [[1]]
#    
#    #Starting value.    
#    value = 2
#    
#    #Called when beginning a new ring.
#    def new_ring(grid, value):
#        grid = grid
#        value = value
#        grid.insert(0,[])
#        grid.append([])
#        
#        for row in range(1,len(grid)):
#            grid[row].append(value)
#            value += 1
#        
#        for i in range(len(grid) - 1):
#            grid[-1].insert(0,value)
#            value += 1
#            
#        for row in range(len(grid)-1,-1,-1):
#            grid[row].insert(0,value)
#            value += 1
#            
#        for i in range(len(grid) - 1):
#            grid[0].append(value)
#            value += 1
#        
#        return grid
    
def new_ring(g):
    value = g[0][-1] + 1
    
    grid=[]
    for row in g:
        grid.append([])
        for val in row:
            grid[-1].append(val)
        
    grid.insert(0,[])
    grid.append([])
    
    for row in range(1,len(grid)):
        grid[row].append(value)
        value += 1
    
    for i in range(len(grid) - 2):
        grid[-1].insert(0,value)
        value += 1
        
    for row in range(len(grid)-1,-1,-1):
        grid[row].insert(0,value)
        value += 1
        
    for i in range(len(grid) - 1):
        grid[0].append(value)
        value += 1
    
    return grid


def make_spiral(n):
    spiral = [[1]]
    for i in range(n):
        spiral = new_ring(spiral)
    return spiral


def make_spiral_of_size(n):
    if (n < 0) or (n % 2 != 1):
        raise Exception("n must be an odd natural number.")
    n = (n - 1) >> 1
    return make_spiral(n)


def make_spiral_list(n):
    spiral_list = [[[1]]]
    for i in range(n):
        spiral_list.append(new_ring(spiral_list[-1]))
    return spiral_list



def diag_sum(grid):
    diag_sum = -1
    #Offset for counting the center twice.

    l = len(grid)
    if l == 1:
        return grid[0][0]
    for i in range(l):
        diag_sum += (grid[i][i] + grid[-(i+1)][i])
    return diag_sum