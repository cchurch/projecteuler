#!/usr/bin/env python
"""
Problem 15
19 April 2002

Starting in the top left corner of a 2 x 2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

How many routes are there through a 20 x 20 grid?

http://projecteuler.net/index.php?section=problems&id=15
"""

import math

def grid_routes(x, y):
    return math.factorial(x + y) / (math.factorial(x) * math.factorial(y))

if __name__ == '__main__':
    print grid_routes(1, 1), '(==2)'
    print grid_routes(2, 2), '(==6)'
    print grid_routes(3, 3), '(==20)'
    print grid_routes(20, 20), '(==???)'
