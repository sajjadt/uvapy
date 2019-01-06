from math import sqrt, acos, pow

# area of ellipse
# pi * a * b

num_tests = int(input())
pi = 2 * acos(0)

for i in range(num_tests):
  d, l = list(map(int, input().split()))

  a = sqrt( pow(l/2, 2) - pow(d/2,2))
  b = l / 2
  area = pi * a * b

  print("{:.3f}".format(area))
  