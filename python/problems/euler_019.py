"""Project Euler - Problem 15

You are given the following information:

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime


def Euler019():
  start = datetime.date(1901, 1, 1)
  end = datetime.date(2000, 12, 31)
  diff = (end - start).days

  suns = 0

  for i in range(diff + 1):
    ns = start + datetime.timedelta(days=i)
    if ns.weekday() == 6 and ns.day == 1:
      suns += 1

  return suns


if __name__ == '__main__':
  print Euler019()
