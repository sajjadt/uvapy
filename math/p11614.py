from math import sqrt

num_tests = int(input())

for i in range(num_tests):
  num = int(input())
  root = int(sqrt(2 * num))

  if (root*(root+1)) // 2 > num:
    root -= 1

  print(root)

