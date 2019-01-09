from math import sqrt, isclose


def triangle_area(a, b, c):
  ''' Using Heron's formula'''
  s = a + b + c
  s /= 2

  return sqrt(s * (s - a) * (s -b) * (s - c))
  
while True:
  try:
    a, b, c = list(map(float, input().split()))

    if isclose(a, 0) or isclose(b, 0) or isclose(c, 0):
      r = 0
    else:
      area = triangle_area(a, b, c)
      r = 2 * area / (a + b + c)
    print("The radius of the round table is: {:.3f}".format(r))

  except(EOFError):
    break