import time
from sys import stdout

def fill_table(max_n, max_k):
  # O(n*n*k)
  #  ---  N ---
  # |
  #  K
  # |___  N ___
  table = [[0]*(max_n+1) for i in range(max_k+1)]
  
  # Init table
  for i in range(max_n+1):
    table[1][i] = 1
  for i in range(max_k + 1):
    table[i][0] = 1
  
  for k in range(2, max_k+1):
    for n in range(1, max_n+1):
      table[k][n] = sum(table[k-1][:n+1]) % 1000000
  return table

MAX_N = 100
MAX_K = 100

# s = time.time()
table = fill_table(MAX_N, MAX_K)
# e = time.time()
# print(e - s)
while True:
  n, k = list(map(int, input().split()))
  if n == k == 0:
    break

  stdout.write("{}\n".format(table[k][n]))