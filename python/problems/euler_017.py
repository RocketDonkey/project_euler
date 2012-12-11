"""Project Euler - Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
                                                        forty-two) contains 23
letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and"
when writing out numbers is in compliance with British usage.
"""


NUM_MAP = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    1000: 11
    }

def MapNum(n):
  """Map each number to its corresponding number of characters."""

  for num in range(n, n+1):
    str_num = str(num)
    mapper = NUM_MAP.get(num, None)

    if mapper:
      return mapper
    else:
      if len(str_num) == 3:
        h, t, o = map(lambda x: int(x[1]) * 10**(2-x[0]), enumerate(str_num))
        if not any([t, o]):
          return NUM_MAP[h/100] + 7
        else:
          two_map = int(str_num[1:])
          stub = NUM_MAP[h/100] + 3 + 7
          if NUM_MAP.get(two_map, None):
            return stub + NUM_MAP[two_map]

          if not t:
            return stub + NUM_MAP[o]
          elif not o:
            return stub + NUM_MAP[t]
          else:
            return stub + NUM_MAP[t] + NUM_MAP[o]

      # 2-digits
      elif len(str_num) == 2:
        tens, ones = int(str_num[0])*10, int(str_num[1])
        return NUM_MAP[tens] + NUM_MAP[ones]


def Euler017():
  return sum(MapNum(n) for n in range(1, 1001))


if __name__ == '__main__':
  print Euler017()
