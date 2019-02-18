from sys import stdin, stdout

num_cases = int(stdin.readline().strip())

for c in range(num_cases):

  stdin.readline().strip()

  rows, cols = list(map(int, stdin.readline().strip().split()))

  # 1 indicates that road is blocked
  b_map = [[0]*cols for i in range(rows)]
  for r in range(rows):
    line = stdin.readline().strip().split()
    for x in line[1:]:
      b_map[r][int(x)-1] = 1

  # Counts number of ways to reach the destination from each location
  dp_map = [[0]*cols for i in range(rows)]

  dp_map[-1][-1] = 1 if b_map[-1][-1] == 0 else 0

  for col in reversed(range(cols)):
    for row in reversed(range(rows)):
      if b_map[row][col] == 1:
        continue

      if row < rows - 1:
        dp_map[row][col] += dp_map[row+1][col]
      if col < cols - 1:
        dp_map[row][col] += dp_map[row][col+1]
  
  if c > 0:
    stdout.write("\n")
  stdout.write("{}\n".format(dp_map[0][0]))
