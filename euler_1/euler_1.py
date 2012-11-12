"""Project Euler - Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import timeit


def Compress(n, multiple):
  series = n/multiple
  return (multiple*series*(series+1))/2


def CorrectAnswer():
  target = 999
  five = Compress(target, 5)
  three = Compress(target, 3)
  fif = Compress(target, 15)
  return five + three - fif


def MyAnswer():
  num = 1000
  r = range(3, num)

  for index, i in enumerate(xrange(3, num)):
    if sum(bool(j) for j in (i%3, i%5)) > 1:
      r[index] = 0

  return sum(r)


def main():
  mine = timeit.Timer(MyAnswer)
  correct = timeit.Timer(CorrectAnswer)
  my_time = mine.timeit(number=1000)
  correct_time = correct.timeit(number=1000)
  print 'My time: {0}'.format(my_time)
  print 'Correct time: {0}'.format(correct_time)


if __name__ == '__main__':
  main()
