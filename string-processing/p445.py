from sys import stdin, stdout

def process_line(line):
  count = 0
  current = ""
  out = []
  for ch in line:
    if ch.isdigit(): #
      count += int(ch)
    elif ch == "!": # New line
      out.append(current)
      current = ""
      count = 0
    else:
      if ch == "b":
        current += count * " "
      else:
        current += count * ch
      count = 0
  
  out.append(current)
  return out

def print_maze(maze):
  print("\n".join("".join(x) for x in maze))

maze = []
while True:
  line = stdin.readline()
  if line == "": # End of input
    print_maze(maze)
    break
  
  line = line.strip()
  if line == "": # End of current maze
    print_maze(maze)
    print()
    maze = []
  else:
    maze += process_line(line)

