"""Project Euler - Problem 9

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

from itertools import combinations


def main():
  """The two formulas are a system of equations, which result in:

     1000a - ab + 1000b = 500000

     The highest value an item can be without going over is 499, so
     that is our upper bound.
     """

  for s in combinations(range(1, 500), 2):
    # Calculate formula
    if (1000*s[0]) - (s[0]*s[1]) + (1000*s[1]) == 500000:
      a, b, c = s[0], s[1], int(math.sqrt(s[0]**2 + s[1]**2))
      print 'Nums: {0}, {1}, {2} | Product: {3}'.format(a, b, c, a*b*c)


if __name__ == '__main__':
  main()
