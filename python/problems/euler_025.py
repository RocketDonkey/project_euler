"""One-line documentation for euler_025 module.

A detailed description of euler_025.
"""



def Fib(n):
  prev = 1
  p_prev = 1
  result = [1, 1]
  for i in range(n):
    result.append(prev + p_prev)
    prev, p_prev = prev + p_prev, prev

  return result


def Euler025():
  for index, i in enumerate(Fib(300000)):
    if len(str(i)) == 1000:
      return index + 1


if __name__ == '__main__':
  print Euler025()
