from sys import stdout
# Similar to p357
coin_types = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

def fill_table(table_size):
  coins = [x//5 for x in coin_types]
  table = [[0] * table_size for c in coins]

  table[0] = [1] * table_size
  
  for ci, cv in enumerate(coins):
    if ci == 0:
      continue
    for n in range(0, table_size):
      table[ci][n] = table[ci-1][n] + (table[ci][n-cv] if n >= cv else 0)  
  return table

table = fill_table(30000//5+1)

while True:
  try:
    n = float(input())
    if n == 0:
      break
    v = table[len(coin_types)-1][int(n*20)]
    stdout.write("{:>6.2f} {:>16}\n".format(n, v))
    
  except(EOFError):
    break