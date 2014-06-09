#!/usr/bin/env python
"""
Problem 5
30 November 2001

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

http://projecteuler.net/index.php?section=problems&id=5
"""

from p3 import primes

def decompose_primes(n):
    factors = []
    for p in primes(n):
        if n % p == 0:
            factors.append(p)
            if n / p > 1:
                factors.extend(decompose_primes(n / p))
            break
    return factors

def least_common_multiple(n):
    factors = []
    for x in xrange(2, n + 1):
        pf = decompose_primes(x)
        for p in set(pf):
            while factors.count(p) < pf.count(p):
                factors.append(p)
    r = 1
    for f in factors:
        r *= f
    return r

if __name__ == '__main__':
    print least_common_multiple(10)
    print least_common_multiple(20)
