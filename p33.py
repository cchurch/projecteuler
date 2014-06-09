#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Digit canceling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

http://projecteuler.net/problem=33
"""

if __name__ == '__main__':
    nums = []
    dems = []
    for x in xrange(10, 100):
        for y in xrange(x, 100):
            xdigits = [c for c in str(x)]
            ydigits = [c for c in str(y)]
            for d in set(xdigits) & set(ydigits):
                newx = int(str(x).replace(d, '') or d)
                newy = int(str(y).replace(d, '') or d)
                if newy == 0 or d == '0' or x == y:
                    continue
                if 1.0 * x / y == 1.0 * newx / newy:
                    print x, '/', y, '==', newx, '/', newy
                    nums.append(newx)
                    dems.append(newy)
    num = reduce(lambda x, y: x * y, nums)
    dem = reduce(lambda x, y: x * y, dems)
    for z in xrange(num, 0, -1):
        if num % z == 0 and dem % z == 0:
            num, dem = num / z, dem / z
            break
    print num, '/', dem
