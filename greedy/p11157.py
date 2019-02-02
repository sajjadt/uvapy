from time import time
from sys import stdin, stdout

buffer = []
def get_next_tokens(n):
  ''' Returns a list contains next n integers read from the console '''
  global buffer

  while len(buffer) < n:
    inp = stdin.readline().strip()
    if inp == "" :
      continue
    else:
      buffer += inp.split()
      
  ret =  buffer[0:n]
  buffer = buffer[n:]
  
  return ret


s = time()
num_cases = int(input())

for t in range(num_cases):
  n, d = list(map(int, input().split()))
  
  stones = [['B', 0]] + [[p[0], int(p[1])] for p in [x.split("-") for x in get_next_tokens(n)]] + [['B', d]]

  max_leap = 0
  for i in range(1, len(stones)): 
    if stones[i][0] == 'B':
      if stones[i-1][0] == 'B':
        max_leap = max(max_leap, stones[i][1] - stones[i-1][1])
      elif i > 1:
        max_leap = max(max_leap, stones[i][1] - stones[i-2][1])
    else:
      if i > 1 and stones[i-1][0] == 'S':
        max_leap = max(max_leap, stones[i][1] - stones[i-2][1])
  stdout.write("Case {}: {}\n".format(t+1, max_leap))
e = time()

# print(e - s)