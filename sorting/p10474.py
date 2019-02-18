from bisect import bisect_left
from sys import stdin, stdout

def _input():
  line = stdin.readline().strip()
  while line == "":
    line = stdin.readline().strip()
  return line

def find_ge_index(a, x):
  'Find leftmost value greater than or equal to x'
  i = bisect_left(a, x)
  if i < len(a) and a[i] == x:
    return i
  return -1

case = 1
while True:
  n, q = list(map(int, _input().split()))

  if n == q == 0:
    break

  numbers = []
  for i in range(n):
    numbers.append(int(_input()))

  numbers.sort()
  stdout.write("CASE# {}:\n".format(case))
  for i in range(q):
    query = int(_input())
    index = find_ge_index(numbers, query)
    if index == -1:
      stdout.write("{} not found\n".format(query))
    else:
      stdout.write("{} found at {}\n".format(query, index + 1))
  case += 1