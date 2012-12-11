"""Project Euler - Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def Euler001():
  num = 1000
  r = range(3, num)

  for index, i in enumerate(xrange(3, num)):
    if sum(bool(j) for j in (i%3, i%5)) > 1:
      r[index] = 0

  return sum(r)


def main():
  print Euler001()


if __name__ == '__main__':
  main()
