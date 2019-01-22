
# Fill 2d table for a fixed m 
def fill_table(max_k, max_n, m):
  table = [ [0] * (max_n+1) for i in range(max_k+1) ]
  
  # Recursive equation: F(k, n) = sum (F (k-1, n-i)) for i in [1..m]
  # Init table
  for i in range(m):
    table[1][i+1] = 1

  for k in range(2, max_k+1):
    for n in range(1, max_n + 1):
      total = 0
      for i in range(max(0, n-m), n):
        total += table[k-1][i] 
      table[k][n] = total 

  return table

MAX_N = MAX_K = MAX_M = 50

table = []
for m in range(MAX_M + 1):
  table.append(fill_table(MAX_K, MAX_N, m))

while True:
  try:
    n, k, m = list(map(int, input().split()))
    print(table[m][k][n])
  except(EOFError):
    break
