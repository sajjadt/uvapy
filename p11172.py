from math import ceil
num_tests = int(input())

for test in range(num_tests):
  a, b = list(map(int, input().split()))
  print(">" if a > b else "<" if a < b else "=")


