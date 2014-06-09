#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Self powers
Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

http://projecteuler.net/problem=48
"""

if __name__ == '__main__':
    s1 = sum(n**n for n in xrange(1, 11))
    assert s1 == 10405071317
    s2 = sum(n**n for n in xrange(1, 1001))
    print s2 % 10000000000
