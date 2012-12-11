"""Project Euler - Problem 15

Starting in the top left corner of a 2x2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
"""


class Memoize(object):
  """Cache numbers from Factorial."""
  def __init__(self, func):
    self.func = func
    self.cache = {}

  def __call__(self, num):
    if num in self.cache:
      return self.cache[num]
    self.cache[num] = self.func(num)

    return self.cache[num]


@Memoize
def Factorial(num):
  if num == 1:
    return 1
  else:
    return num * Factorial(num - 1)


def BinomialCoefficient(n):
  """Central Binomial Coefficient - 2, 6, 20, ...

  Compute the CBC for a given number. Formula is:

      (2n)!
      ----
      (n!)**2
  """

  return Factorial(2*n) / (Factorial(n))**2


def Euler015():
  """Print the BC of the number of squares on a side of the grid."""
  return BinomialCoefficient(20)


if __name__ == '__main__':
  print Euler015()
