from collections import Counter
from sys import stdin, stdout  
from time import time

def last_nonzero(lst):
  for i, value in enumerate(reversed(lst)):
    if value != 0:
      return (len(lst)-i-1), value
  return -1, None

start = time()

while True:
  try:
    n = int(stdin.readline().strip())

    if n == 0:
      break

    freq = [0] * (n + 1)
    courses = Counter()
    for i in range(n):
      line = sorted(list(map(int, stdin.readline().strip().split())))
      hash_key = tuple(line)

      courses[hash_key] += 1
      freq[courses[hash_key]] += 1
      freq[courses[hash_key]-1] -= 1
    
    last = last_nonzero(freq)
    stdout.write("{}\n".format(last[0]*last[1]))
  except(EOFError):
    break

end = time()
# print(end - start)