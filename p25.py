#!/usr/bin/env python
"""
Problem 25
30 August 2002

The Fibonacci sequence is defined by the recurrence relation:

F n = F n-1 + F n-2, where F 1 = 1 and F 2 = 1.

Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

http://projecteuler.net/problem=25
"""

def fibonacci():
    x = 1
    y = 1
    yield x
    yield y
    while True:
        z = x + y
        yield z
        x = y
        y = z

if __name__ == '__main__':
    for n, f in enumerate(fibonacci()):
        print n + 1, f
        if len(str(f)) == 3:
            print n + 1
            break
    for n, f in enumerate(fibonacci()):
        print n + 1, f
        if len(str(f)) == 1000:
            print n + 1
            break
