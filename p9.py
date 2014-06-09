#!/usr/bin/env python
"""
Problem 9
25 January 2002

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

http://projecteuler.net/index.php?section=problems&id=9
"""

def pythagorean_triplets(max=1000):
    for a in xrange(1, max):
        for b in xrange(a + 1, max):
            for c in xrange(b + 1, max):
                if (a**2 + b**2) == c**2:
                    yield a, b, c

if __name__ == '__main__':
    for pt in pythagorean_triplets():
        if sum(pt) == 1000:
            print pt
            print pt[0] * pt[1] * pt[2]
            break
