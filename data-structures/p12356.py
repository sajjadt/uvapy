import time
from sys import stdin, stdout

next_array = [i for i in range(1, 100000 + 2)]
prev_array = [i for i in range(-1, 100000) ]
prev_array[0] = -1

while True:
  n, q = list(map(int, stdin.readline().strip().split()))

  if n == q == 0:
    break

  for i in range(1, n+1):
    next_array[i] = i + 1
    prev_array[i] = i - 1
  next_array[n] = -1
  
  for j in range(q):
    start, end = list(map(int, stdin.readline().strip().split()))

    # kill soldiers in range start, end
    prev = prev_array[start]
    nex = next_array[end]

    if prev > 0:
      next_array[prev] = next_array[end]
    
    if nex > 0:
      prev_array[nex] = prev_array[start]

    stdout.write("{} {}\n".format(prev_array[start] if prev > 0 else "*", next_array[end] if nex > 0 else "*"))
  stdout.write("-\n")
