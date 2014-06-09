#!/usr/bin/env python
"""
Problem 10
08 February 2002

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

http://projecteuler.net/index.php?section=problems&id=10
"""

def primes(max=None):
    """Return a generator of prime numbers up to the given maximum."""
    p = map(lambda x: True, xrange(0, max + 1))
    p[0] = False
    p[1] = False
    for n, x in enumerate(p):
        if not x:
            continue
        yield n
        for y in xrange(n, max + 1, n):
            p[y] = False

if __name__ == '__main__':
    print sum(primes(10))
    print sum(primes(2000000))
