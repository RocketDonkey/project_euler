"""Project Euler - Problem 22

Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.

Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""


def Euler022():
  with open('./data/names.txt', 'rb') as f:
    contents = sorted([n.strip('"') for n in f.read().split(',')])

  d = dict((chr(i), i-96) for i in range(97, 123))

  name_sum = 0
  for index, name in enumerate(contents):
    name_sum += (sum(map(lambda x: d[x], name.lower())) * (index+1))

  return name_sum


if __name__ == '__main__':
  print Euler022()
