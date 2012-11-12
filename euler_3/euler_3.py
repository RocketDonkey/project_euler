"""Project Euler - Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import timeit


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
