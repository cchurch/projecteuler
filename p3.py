#!/usr/bin/env python
"""
Problem 3
02 November 2001

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

http://projecteuler.net/index.php?section=problems&id=3
"""

import sys

def primes(max=None):
    """Return a generator of prime numbers up to the given maximum."""
    m = max or sys.maxint
    p = [2, 3]
    for n in p:
        yield n
    while n < m:
        n += 1
        if any(n % x == 0 for x in p):
            continue
        p.append(n)
        yield n

def prime_factors(n):
    """Return all the prime factors of the given number n.
    
    Algorithm from: http://en.wikipedia.org/wiki/Trial_division
    """
    for p in primes(int(n**0.5) + 1):
        if p*p > n:
            break
        while n % p == 0:
            yield p
            n //= p
    if n > 1:
        yield n

if __name__ == '__main__':
    print 'prime factors of 13195 are', list(prime_factors(13195))
    print 'largest prime factor of 600851475143 is', max(prime_factors(600851475143))
