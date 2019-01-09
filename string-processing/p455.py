# Compare with string-processing/p10298

import re

# start_time = time.time()
num_cases = int(input())
  
for test in range(num_cases):

  input()
  s = input()

  power = len([m.start() for m in re.finditer('(?={})'.format(s), s + s)]) - 1

  print(len(s) // power)
  if test < num_cases -1 :
    print()
# end_time = time.time()
# print(end_time - start_time)