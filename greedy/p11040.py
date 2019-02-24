def solve(a, b, c):
  #      a
  #     x  y
  #   b   z   c
  z = (a - b- c)//2
  x = z + b
  y = z + c
  return x, y, z

cases = int(input())
for c in range(cases):
  wall = []
  for i in range(5):
    wall.append(list(map(int, input().split())))

  complete_wall = [wall[0]]
  for i in range(len(wall) - 1):
    for j in range(len(wall[i])):
      # append x,y,b,z,c to output wall (a is added in the previous iteration)
      a, b, c = wall[i][j], wall[i+1][j], wall[i+1][j+1]
      x,y,z = solve(a, b, c)
      if len(complete_wall) != 2*i+3:
        complete_wall.append([x, y])
        complete_wall.append([b, z, c])
      else:
        complete_wall[-2] += [x, y]
        complete_wall[-1] += [z, c]
  print("\n".join([" ".join(map(str, x)) for x in complete_wall]))
