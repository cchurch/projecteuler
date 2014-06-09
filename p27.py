#!/usr/bin/env python
"""
Problem 27
27 September 2002

Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula n^2 - 79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.

http://projecteuler.net/problem=27
"""

from p3 import primes

_p2 = []

def primes2():
    if _p2:
        for p in _p2:
            yield p
        p0 = p
    else:
        p0 = 0
    for p in primes():
        if p > p0:
            _p2.append(p)
            yield p

def q(a, b, n):
    return n**2 + (a * n) + b

def nprimes(a, b):
    for n in xrange(0, 1000000):
        r = q(a, b, n)
        for p in primes2():
            if p > r:
                return n
            elif p == r:
                break

if __name__ == '__main__':
    az, bz, nz = 0, 0, 0
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            z = nprimes(a, b)
            print a, b, z
            if z > nz:
                az, bz, nz = a, b, z
    print 'MAX', az, bz, nz
    print 'a*b =', az * bz
