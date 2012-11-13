"""Project Euler - Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""
import math


def Eratosthenes(n):

  # Skip all multiples of two since they won't count
  numlist = range(3, n+1, 2)

  # In numlist, toggle non-primes to 0
  backup = 0
  for index, num in enumerate(numlist):
    counter = backup
    if num:
      counter += num
      while counter <= len(numlist)-1:
        numlist[counter] = 0
        counter += num
    backup += 1
    if index > 10000:
      break
  return filter(bool, numlist)

def main():
  # Pick an arbitrary high number that will have at least 10,001 primes
  main = 100000000000
  num = int(math.sqrt(main))
  l = Eratosthenes(num)
  print l[9999]


if __name__ == '__main__':
  main()
