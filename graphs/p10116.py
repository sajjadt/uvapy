
while True:
  rows, cols, start_col = list(map(int, input().split()))

  if rows == cols == start_col == 0:
    break

  grid = []
  seen_at = [[0]*cols for i in range(rows)]
  for i in range(rows):
    grid.append(list(input()))

  in_range = lambda row, col: row >= 0 and col >= 0 and row < rows and col < cols

  pos_row, pos_col = 0, start_col - 1
  step = 1
  while in_range(pos_row, pos_col) and seen_at[pos_row][pos_col] == 0: 
    seen_at[pos_row][pos_col] = step
    step += 1
    direction = grid[pos_row][pos_col]
    pos_row = pos_row + 1 if direction == "S" else pos_row - 1 if direction == "N" else pos_row
    pos_col = pos_col + 1 if direction == "E" else pos_col - 1 if direction == "W" else pos_col

  if not in_range(pos_row, pos_col):
    print("{} step(s) to exit".format(step-1))
  else:
    print("{} step(s) before a loop of {} step(s)".format(seen_at[pos_row][pos_col] - 1, step - seen_at[pos_row][pos_col]))
