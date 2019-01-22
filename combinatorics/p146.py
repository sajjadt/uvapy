from sys import stdin, stdout

while True:
  inp = stdin.readline().strip()

  if inp == "#":
    break

  successor = None
  inp = list(inp)
  for i in range(len(inp)-1, 0, -1):
    if ord(inp[i]) > ord(inp[i-1]):

      successor = ("".join(inp[0:i-1]) if i > 1 else "")

      min_v, min_i = inp[i], i
      for j in range(i, len(inp)):
        if inp[j] < min_v and inp[j] > inp[i-1]:
          min_v, min_i = inp[j], j
      
      
      successor += min_v
      inp[min_i] = inp[i-1]
      successor += "".join(sorted(inp[i:]))
      break
  
  if successor:
    stdout.write("{}\n".format(successor))
  else:
    stdout.write("No Successor\n")