from collections import deque
from sys import stdin, stdout


num_cases = int(stdin.readline().strip())

for c in range(num_cases):
  n, m, l = list(map(int, stdin.readline().strip().split()))
  
  next_d = [set([]) for i in range(n)]
  for i in range(m):
    u, v = list(map(int, stdin.readline().strip().split()))
    if u != v:
      next_d[u-1].add(v-1)
  
  fell = set([])
  Q = deque([])

  # start with l
  for i in range(l):
    f = int(stdin.readline().strip())
    Q.append(f-1)
    fell.add(f-1)
  
  while len(Q) > 0:
    top = Q.pop()

    if len(next_d[top]) > 0:
      for v in next_d[top]:
        if not v in fell:
          fell.add(v)
          Q.appendleft(v)

  stdout.write("{}\n".format(len(fell)))

