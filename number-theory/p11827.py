from math import gcd
from itertools import combinations

num_cases = int(input())
for t in range(num_cases):
  numbers = map(int, input().split())
  res = max([gcd(x, y) for x,y in combinations(numbers, 2)])
  print(res)