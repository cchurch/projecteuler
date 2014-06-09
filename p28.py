#!/usr/bin/env python
"""
Problem 28
11 October 2002

Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?

http://projecteuler.net/problem=28
"""

def sum_of_corners(n):
    corners = range(n**2, (max(0, n - 2))**2, 1 - n or -1)
    return sum(corners)

def sum_of_diagonals(n):
    return sum([sum_of_corners(x) for x in xrange(n, 0, -2)])

if __name__ == '__main__':
    for x in xrange(1, 6, 2):
        print x, sum_of_diagonals(x)
    print 1001, sum_of_diagonals(1001)
