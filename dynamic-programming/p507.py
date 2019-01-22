import operator
from sys import stdin, stdout

num_tests = int(input())    
for test in range(num_tests):
  
  num_routes = int(input())

  # Linear scan to find the largest increase 
  # kadane loop
  total = ans = 0
  start = 0
  last_l = 1
  for i in range(0, num_routes-1):
    total += int(stdin.readline().strip())
    if total > ans:
      ans = total
      start = last_l
      end = i + 2
    elif total == ans:
      if i + 2 - last_l > end - start:
        start = last_l
        end = i + 2

    if total  < 0:
      total = 0
      last_l = i + 2

  if ans > 0:
    stdout.write("The nicest part of route {} is between stops {} and {}\n".format(test+1, start, end))
  else:
    stdout.write("Route {} has no nice parts\n".format(test+1))

