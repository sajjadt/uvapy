# Compare with string-processing/p455

import re
import math
# import time

def divisorGenerator(n):
  large_divisors = []
  for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0:
      yield i
      if i*i != n:
        large_divisors.append(n // i)
  for divisor in reversed(large_divisors):
    yield divisor



# start_time = time.time()
while True:
  s = str(input())

  if s == ".":
    break

  # One line solution exceeds the time limit.
  # print(len([m.start() for m in re.finditer('(?={})'.format(s), s + s)]) - 1)
  
  for l in divisorGenerator(len(s)):
    power = len(s) // l
    found_power = True

    for i in range(power):
      if s[0:l] != s[i*l:i*l+l]:
        found_power = False
        break

    if found_power:
      break
  
  print(power)
# end_time = time.time()
# print(end_time - start_time)