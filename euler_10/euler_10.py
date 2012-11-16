"""Project Euler - Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math


def Eratosthenes(n):

  # Skip all multiples of two since they won't count
  numlist = range(3, n+1, 2)

  # In numlist, toggle non-primes to 0
  backup = 0
  for num in numlist:
    counter = backup
    if num:
      counter += num
      while counter <= len(numlist)-1:
        numlist[counter] = 0
        counter += num
    backup += 1
  return sum([2] + filter(bool, numlist))


def main():
  print Eratosthenes(2000000)


if __name__ == '__main__':
  main()
