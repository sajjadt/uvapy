from math import ceil
num_tests = int(input())

for test in range(num_tests):
  n, m = list(map(int, input().split()))
  sol = ceil((n-2) / 3) * ceil( (m-2)/ 3) 
  print(int(sol))

