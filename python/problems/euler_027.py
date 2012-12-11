"""Project Euler - Problem 27

Euler published the remarkable quadratic formula:

  n² + n + 41

  It turns out that the formula will produce 40 primes for the consecutive
  values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
  divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible
  by 41.

  Using computers, the incredible formula  n²  79n + 1601 was discovered, which
  produces 80 primes for the consecutive values n = 0 to 79. The product of the
  coefficients, 79 and 1601, is 126479.

  Find the product of the coefficients, a and b, for the quadratic expression
  that produces the maximum number of primes for consecutive values of n,
  starting with n = 0.

"""

from primes import primes


def main():
  ps = set(primes.Eratosthenes(1000000))
  form = :wq
  for i in ps:
    n = str(i)
    if all([1 if int(n[-j:] + n[:-j]) in ps else 0 for j in xrange(len(n))]):
      s.add(i)

  print len(s)


if __name__ == '__main__':
  main()
