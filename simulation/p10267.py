from sys import stdin, stdout

image = []
while True:
  ins = stdin.readline().strip().split()
  
  if ins[0] == "I":
    cols, rows = int(ins[1]), int(ins[2])
    image = [['O']*cols for r in range(rows) ]

  elif ins[0] == "C":
    image = [['O']*cols for r in range(rows) ]

  elif ins[0] == "L":
    x, y = int(ins[1])-1, int(ins[2])-1
    c = ins[3]
    image[y][x] = c
  
  elif ins[0] == "V":
    x, y1, y2 = int(ins[1])-1, int(ins[2])-1, int(ins[3])-1
    c = ins[4]
    for i in range(min(y1, y2), max(y1, y2)+1):
      image[i][x] = c

  elif ins[0] == "H":
    x1, x2, y = int(ins[1])-1, int(ins[2])-1, int(ins[3])-1
    c = ins[4]
    for i in range(min(x1, x2), max(x1, x2)+1):
      image[y][i] = c

  elif ins[0] == "K":
    x1, y1, x2, y2 = int(ins[1])-1, int(ins[2])-1, int(ins[3])-1, int(ins[4])-1
    c = ins[5]
    for i in range(min(x1, x2), max(x1, x2)+1):
      for j in range(min(y1, y2), max(y1, y2)+1):
        image[j][i] = c

  elif ins[0] == "F":
    x, y = int(ins[1])-1, int(ins[2])-1
    new_color = ins[3]
    p = (y, x)
    color = image[p[0]][p[1]]
    
    if color == new_color:
      continue

    image[p[0]][p[1]] = new_color
    q = [p]

    while len(q) > 0:
      r, c = q.pop()
      image[r][c] = new_color
      if r > 0 and image[r-1][c] == color:
        q.append((r-1, c))
      if r < rows - 1 and image[r+1][c] == color:
        q.append((r+1, c))
      if c > 0 and image[r][c-1] == color:
        q.append((r, c-1))
      if c < cols - 1 and image[r][c+1] == color:
        q.append((r, c+1))

  elif ins[0] == "S":
    name = ins[1]
    stdout.write("{}\n{}\n".format(name, "\n".join(["".join(row) for row in image])))

  elif ins[0] == "X":
    break

  else:
    continue

