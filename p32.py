#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

http://projecteuler.net/problem=32
"""

def pandigital_products(n):
    for x in xrange(1, 3**n + 1):
        for y in xrange(x, 3**n + 1):
            z = x * y
            digits = sorted([int(c) for c in (str(x) + str(y) + str(z))])
            if len(digits) > (n + 1):
                break
            #print '%d x %d = %d' % (x, y, z)
            #print ''.join(digits), range(1, n + 1)
            if digits == range(1, n + 1):
                print '*** %d x %d = %d' % (x, y, z)
                yield z

if __name__ == '__main__':
    products = set()
    for z in pandigital_products(9):
        products.add(z)
    print '==', sum(products)
