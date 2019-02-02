from sys import stdin, stdout
import time
from bisect import bisect_right

s_t = time.time()
candidates = stdin.readline()

def find_gt(a, x):
  'Find leftmost value greater than x'
  i = bisect_right(a, x)
  if i != len(a):
    return a[i]
  return -1

# 'z' > 'Z'
indices = [[] for i in range(ord('z')+1)]
for i, ch in enumerate(candidates):
  indices[ord(ch)].append(i)

n_queries = int(input())
for i in range(n_queries):
  query = stdin.readline().strip()
  
  global_index = -1
  for i, ch in enumerate(list(query)):
    global_index = find_gt(indices[ord(ch)], global_index)
    if global_index == -1:
      s = e = -1
      break
    if i == 0:
      s = global_index
    if i == len(query) - 1:
      e = global_index
  
  if s == e == -1:
    stdout.write("Not matched\n")
  else:
    stdout.write("Matched {} {}\n".format(s, e))

e_t = time.time()
# print(e_t - s_t)