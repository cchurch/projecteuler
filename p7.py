#!/usr/bin/env python
"""
Problem 7
28 December 2001

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?

http://projecteuler.net/index.php?section=problems&id=7
"""

from p3 import primes

def prime_at_position(i):
    for n, p in enumerate(primes()):
        if n + 1 == i:
            return p

if __name__ == '__main__':
    print prime_at_position(6)
    print prime_at_position(10001)
