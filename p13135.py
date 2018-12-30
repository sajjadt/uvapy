from math import sqrt, floor

num_tests = int(input())

for i in range(num_tests):
  s = int(input())

  s *= 2
  n = int(floor(sqrt(s)))
  if n*(n +1) == s:
    print(n - 1)
  else:
    print("No solution")
