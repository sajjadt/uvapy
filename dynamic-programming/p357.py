from sys import stdout
# Recursive formula (assuming only 1, 5, 10 coins are available)
# F(N [1,5,10]) = F(N, [1, 5] {largest coin is not used}) + F(N-10, [1, 5, 10]) {largest coin is used}
def fill_table(table_size):
  coins = [1, 5, 10, 25, 50]
  table = [[0] * table_size for c in coins]

  # Init first row and column
  # table[0][c] = ways to construct c only with 1 cents
  # table[1][c] = ways to construct c only with 1, 5 cents
  table[0] = [1] * table_size
  
  for ci, cv in enumerate(coins):
    if ci == 0:
      continue
    for n in range(0, table_size):
      table[ci][n] = table[ci-1][n] + (table[ci][n-cv] if n >= cv else 0)  
  return table

table = fill_table(30000+1)

while True:
  try:
    n = int(input())
    v = table[4][n]
    if v > 1:
      stdout.write("There are {} ways to produce {} cents change.\n".format(v, n))
    else:
      stdout.write("There is only 1 way to produce {} cents change.\n".format(n))
  except(EOFError):
    break