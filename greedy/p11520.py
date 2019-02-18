from string import ascii_uppercase

num_cases = int(input())

for c in range(num_cases):
  dim = int(input())

  grid = []
  for i in range(dim):
    grid.append(list(input().strip()))

  for row in range(dim):
    for col in range(dim):
      if grid[row][col] == '.':
        
        neighbors = []
        if row > 0 and grid[row-1][col] != '.':
          neighbors.append(grid[row-1][col])
        
        if col > 0 and grid[row][col-1] != '.':
          neighbors.append(grid[row][col-1])

        if row < dim - 1 and grid[row+1][col] != '.':
          neighbors.append(grid[row+1][col])

        if col < dim - 1 and grid[row][col+1] != '.':
          neighbors.append(grid[row][col+1])

        for min_ch in ascii_uppercase:
          if not min_ch in neighbors:
            grid[row][col] = min_ch
            break
        
  print("Case {}:".format(c+1))
  print("\n".join(["".join(g) for g in grid]))
