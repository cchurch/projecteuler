#!/usr/bin/env python
"""
Problem 19
14 June 2002

You are given the following information, but you may prefer to do some research
for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September, April, June and November. All the rest have
  thirty-one, Saving February alone, Which has twenty-eight, rain or shine. And
  on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

http://projecteuler.net/problem=19
"""

def dow(y, m, d):
    t = (y - 1900)
    t += sum([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m])
    if y % 4 == 0 and y % 100 != 0:
        t += 1
    t += d
    return t % 7

if __name__ == '__main__':
    print dow(1900, 1, 1), '(==1)'
    print dow(1979, 12, 30), '(==0)'
    print dow(1989, 12, 27), '(==3)'
    count = 0
    for y in xrange(1901, 2001):
        for m in xrange(1, 13):
            #print y, m, dow(y, m, 1)
            if dow(y, m, 1) == 0:
                count += 1
                print y, m, dow(y, m, 1), count,  (y - 1900), (y - 1900) / 4
    print count
    