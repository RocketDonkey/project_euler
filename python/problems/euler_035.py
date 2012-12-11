"""Project Euler - Problem 35

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?

"""

from primes import primes


def Euler035():
  s = set()
  ps = set(primes.Eratosthenes(1000000))
  for i in ps:
    n = str(i)
    if all([1 if int(n[-j:] + n[:-j]) in ps else 0 for j in xrange(len(n))]):
      s.add(i)

  return len(s)


if __name__ == '__main__':
  print Euler035()
