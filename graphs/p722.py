from sys import stdin

num_cases = int(input())
input()

for case in range(num_cases):
  
  r_start, c_start = list(map(int, input().split()))
  g = []
  
  line = stdin.readline().strip()
  while line != "":
    c = list(line)
    g.append(c)
    line = stdin.readline().strip()
  
  rows = len(g)
  cols = len(g[0])
  visited = [[False]*cols for i in range(rows)]

  area = 0
  Q = []
  r_start -= 1
  c_start -= 1
  # print(g)
  if g[r_start][c_start] == '0':
    visited[r_start][c_start] = True
    Q.append((r_start, c_start))
  
  while len(Q) > 0:
    r, c = Q.pop()
    area += 1
    # Left
    if r > 0:
      if not visited[r-1][c] and g[r-1][c] == '0':
        visited[r-1][c] = True
        Q.append((r-1, c))
    # Right
    if r < rows - 1:
      if not visited[r+1][c] and g[r+1][c] == '0':
        visited[r+1][c] = True
        Q.append((r+1, c))
    # Top
    if c > 0:
      if not visited[r][c-1] and g[r][c-1] == '0':
        visited[r][c-1] = True
        Q.append((r, c-1))
    # Bottom
    if c < cols - 1:
      if not visited[r][c+1] and g[r][c+1] == '0':
        visited[r][c+1] = True
        Q.append((r, c+1))

  if case > 0:
    print()
  print(area)
